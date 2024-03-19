from fontTools.ttLib import TTCollection

    
def ttc2ttf(ttc_path, output_dir):
    ttc = TTCollection(ttc_path)
    for i, ttf in enumerate(ttc):
        input_file_name = ttc_path.split("\\")[-1].split(".")[0]
        output_path = output_dir + f"{input_file_name}_{i}.ttf"
        ttf.save(output_path)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ttc2ttf.py <source_font_path>")
        sys.exit(1)
    
    source_font_path = sys.argv[1]
    ttc2ttf(source_font_path, "./output/")