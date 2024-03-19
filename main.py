
import fontforge
import sys

def copy_font_properties(source_font_path, target_font_path, output_path):
    source_font = fontforge.open(source_font_path)

    target_font = fontforge.open(target_font_path)
    print(dir(target_font))
    
    for key in dir(target_font):
        print(key, getattr(target_font, key))
    
    target_font.familyname = source_font.familyname
    target_font.fontname = source_font.fontname
    target_font.fullname = source_font.fullname
    target_font.sfnt_names = source_font.sfnt_names
    target_font.weight = source_font.weight
    target_font.version = source_font.version


    target_font.generate(output_path)

# スクリプトの使用例
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <source_font_path> <target_font_path> <output_path>")
        sys.exit(1)
    
    source_font_path = sys.argv[1]
    target_font_path = sys.argv[2]
    output_path = sys.argv[3]

    copy_font_properties(source_font_path, target_font_path, output_path)