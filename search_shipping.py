with open("knowledge/钧瀚产品优势分级分类总表_dump.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
for idx, line in enumerate(lines):
    if any(k in line for k in ["柜", "箱", "运", "物流"]):
        out_lines.append(f"L{idx+1}: {line.strip()}")

with open("knowledge/search_shipping.txt", 'w', encoding='utf-8') as out_f:
    out_f.write("\n".join(out_lines))

print(f"Successfully wrote {len(out_lines)} lines to search_shipping.txt.")
