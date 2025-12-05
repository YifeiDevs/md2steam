from markdown_it import MarkdownIt
from .converter import markdown_to_steam_bbcode
from .inline_converter import convert_inline

def table_to_bbcode(tokens):
    """Convert table tokens to BBCode"""
    rows, row, is_header = [], [], False

    for i, t in enumerate(tokens):
        if t.type == 'thead_open': is_header = True
        elif t.type == 'thead_close': is_header = False
        elif t.type == 'tr_open': row = []
        elif t.type == 'tr_close': rows.append((row, is_header))
        elif t.type in ('th_open', 'td_open') and i+1 < len(tokens) and tokens[i+1].type == 'inline':
            # 使用现有的 inline converter 处理单元格内的粗体、斜体等
            row.append(convert_inline(tokens[i+1].content))

    if not rows: return ''

    lines = ['[table]']
    for cells, is_h in rows:
        tag = 'th' if is_h else 'td'
        lines.append('[tr]')
        lines.extend(f'[{tag}]{c}[/{tag}]' for c in cells)
        lines.append('[/tr]')
    lines.append('[/table]')
    return '\n'.join(lines)

def markdown_to_steam_with_tables(md_text: str) -> str:
    """Convert Markdown to Steam BBCode with table support"""
    # 启用 table 插件解析
    tokens = MarkdownIt().enable('table').parse(md_text)
    lines, segments, last = md_text.split('\n'), [], -1

    i = 0
    while i < len(tokens):
        if tokens[i].type == 'table_open' and tokens[i].map:
            start, end = tokens[i].map

            # Save text before table
            if start > last + 1:
                # 提取表格前的文本段落
                text = '\n'.join(lines[last+1:start]).strip()
                if text: segments.append(('text', text))

            # Collect table tokens
            table_tokens, depth = [], 1
            i += 1
            while i < len(tokens) and depth > 0:
                if tokens[i].type == 'table_open': depth += 1
                elif tokens[i].type == 'table_close':
                    depth -= 1
                    if depth == 0: break
                table_tokens.append(tokens[i])
                i += 1

            segments.append(('table', table_tokens))
            last = end - 1
        i += 1

    # Save remaining text
    if last + 1 < len(lines):
        text = '\n'.join(lines[last+1:]).strip()
        if text: segments.append(('text', text))

    # 组合结果：普通文本用原有 converter，表格用新函数
    return '\n\n'.join(
        markdown_to_steam_bbcode(s[1]) if s[0] == 'text' else table_to_bbcode(s[1])
        for s in segments
    )
