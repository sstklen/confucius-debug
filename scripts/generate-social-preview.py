#!/usr/bin/env python3
"""
生成 Confucius Debug 的 GitHub Social Preview Image
尺寸：1280 x 640px（GitHub 推薦）
"""

from PIL import Image, ImageDraw, ImageFont
import os

# === 設定 ===
WIDTH, HEIGHT = 1280, 640
BG_COLOR = "#1a1a2e"       # 深藍黑背景
ACCENT_COLOR = "#e94560"    # 紅色強調
ORANGE = "#ff6b35"          # 橘色（品牌色）
WHITE = "#ffffff"
LIGHT_GRAY = "#c4c4c4"
DARK_GRAY = "#16213e"

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "social-preview.png")

# === 建立畫布 ===
img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# === 漸層背景 ===
for y in range(HEIGHT):
    r = int(26 + (22 - 26) * y / HEIGHT)
    g = int(26 + (33 - 26) * y / HEIGHT)
    b = int(46 + (62 - 46) * y / HEIGHT)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

# === 裝飾元素 ===
# 左上角裝飾線
draw.rectangle([(0, 0), (8, HEIGHT)], fill=ORANGE)
# 底部裝飾線
draw.rectangle([(0, HEIGHT - 4), (WIDTH, HEIGHT)], fill=ORANGE)
# 右上角小方塊
draw.rectangle([(WIDTH - 120, 0), (WIDTH, 4)], fill=ACCENT_COLOR)

# === 字型（使用系統字型）===
def get_font(size, bold=False):
    """嘗試多個字型路徑"""
    font_paths = [
        # macOS
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    return ImageFont.load_default()

font_huge = get_font(72, bold=True)
font_large = get_font(36, bold=True)
font_medium = get_font(28)
font_small = get_font(22)

# CJK 字型（中文引言用）
def get_cjk_font(size):
    cjk_paths = [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Songti.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    ]
    for path in cjk_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    return get_font(size)

font_cjk = get_cjk_font(22)

# === 標題 ===
draw.text((60, 45), "CONFUCIUS DEBUG", fill=ORANGE, font=font_huge)

# 副標題
draw.text((60, 135), "AI Debugging That Never Repeats a Mistake", fill=WHITE, font=font_large)

# === 哲學引言（用 CJK 字型）===
# 先量「不貳過」的寬度，動態排版
cjk_text = '不貳過'
cjk_bbox = draw.textbbox((0, 0), cjk_text, font=font_cjk)
cjk_w = cjk_bbox[2] - cjk_bbox[0]

quote_x = 60
draw.text((quote_x, 200), '" ', fill=LIGHT_GRAY, font=font_small)
q1_bbox = draw.textbbox((0, 0), '" ', font=font_small)
q1_w = q1_bbox[2] - q1_bbox[0]

draw.text((quote_x + q1_w, 197), cjk_text, fill=ORANGE, font=font_cjk)
draw.text((quote_x + q1_w + cjk_w + 4, 200), ' " — Never repeat a mistake.  (Analects 6.3)', fill=LIGHT_GRAY, font=font_small)

# === 分隔線 ===
draw.rectangle([(60, 248), (500, 250)], fill=ORANGE)

# === 核心數據 ===
stats = [
    ("980+", "Verified Fixes in KB"),
    ("12", "Platform Specialties"),
    ("FREE", "Search (instant)"),
    ("FREE", "AI Analysis"),
]

x_start = 60
y_pos = 280
box_width = 280
box_height = 120

for i, (number, label) in enumerate(stats):
    x = x_start + (i % 4) * (box_width + 20)
    y = y_pos

    # 數據背景框
    draw.rounded_rectangle(
        [(x, y), (x + box_width, y + box_height)],
        radius=12,
        fill="#16213e",
        outline=ORANGE if i == 0 else "#2a2a4a",
        width=2,
    )

    # 數字
    num_color = ORANGE if number in ("1,143", "FREE") else WHITE
    draw.text((x + 20, y + 15), number, fill=num_color, font=font_large)

    # 標籤
    draw.text((x + 20, y + 70), label, fill=LIGHT_GRAY, font=font_small)

# === 底部區域 ===
# 安裝方式
y_bottom = 440
draw.text((60, y_bottom), "Install:", fill=LIGHT_GRAY, font=font_medium)

methods = [
    ("MCP Server", "#4ade80"),    # 綠
    ("GitHub Action", "#60a5fa"),  # 藍
    ("REST API", "#c084fc"),      # 紫
    ("OpenClaw Skill", "#fb923c"),  # 橘
]

x_pos = 200
for method, color in methods:
    # pill 形狀
    text_bbox = draw.textbbox((0, 0), method, font=font_small)
    tw = text_bbox[2] - text_bbox[0]
    pill_w = tw + 30
    pill_h = 36

    draw.rounded_rectangle(
        [(x_pos, y_bottom + 2), (x_pos + pill_w, y_bottom + pill_h)],
        radius=18,
        fill=color,
    )
    draw.text((x_pos + 15, y_bottom + 5), method, fill="#1a1a2e", font=font_small)
    x_pos += pill_w + 15

# === 準確率 ===
y_acc = 500
draw.text((60, y_acc), "9/9 confirmed correct by maintainers", fill="#4ade80", font=font_medium)
draw.text((60, y_acc + 40), "80-100% accuracy across all 12 platforms", fill=LIGHT_GRAY, font=font_small)

# === 右下角品牌 ===
draw.text((WIDTH - 420, HEIGHT - 55), "washinmura.jp", fill=LIGHT_GRAY, font=font_small)
draw.text((WIDTH - 180, HEIGHT - 55), "MIT License", fill=LIGHT_GRAY, font=font_small)

# === 儲存 ===
img.save(OUTPUT_PATH, "PNG", quality=95)
print(f"✅ Social preview saved: {OUTPUT_PATH}")
print(f"   Size: {WIDTH}x{HEIGHT}px")
