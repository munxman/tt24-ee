#!/usr/bin/env python3
"""Nav redesign script for tt24.ee
Changes:
1. Wrap nav-logo in .nav-brand div + add subtle Meist link near logo
2. Remove Meist from main nav row
3. Make KKK use nav-link--secondary style
4. Add nav-dropdown-toggle--prominent class to Toriistad button
5. Change CTA button text to "Tee eneseanalüüs"
6. index.html: update hero + urgency CTAs
"""
import os
import glob

ROOT = '/Users/lasagnelatte/.openclaw/workspace/tth-portaal'


def process_root_file(filepath):
    """Process a root-level HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Wrap nav-logo in nav-brand + add Meist link (root-level path)
    old_logo = (
        '    <a href="index.html" class="nav-logo" aria-label="TT24 avaleht">\n'
        '      <span class="nav-logo-text">TT24</span>'
        '<span class="nav-logo-tagline">Töötervishoiu Teejuht</span>\n'
        '    </a>'
    )
    new_logo = (
        '    <div class="nav-brand">\n'
        '      <a href="index.html" class="nav-logo" aria-label="TT24 avaleht">\n'
        '        <span class="nav-logo-text">TT24</span>'
        '<span class="nav-logo-tagline">Töötervishoiu Teejuht</span>\n'
        '      </a>\n'
        '      <a href="meist.html" class="nav-brand-meist">Meist</a>\n'
        '    </div>'
    )
    content = content.replace(old_logo, new_logo)

    # 2. Remove Meist from main nav (all variants for root-level)
    content = content.replace(
        '\n      <a href="meist.html" class="nav-link nav-link--secondary">Meist</a>',
        ''
    )
    content = content.replace(
        '\n      <a href="meist.html" class="nav-link nav-link--secondary active">Meist</a>',
        ''
    )

    # 3. KKK -> secondary style
    content = content.replace(
        '<a href="korduma.html" class="nav-link">KKK</a>',
        '<a href="korduma.html" class="nav-link nav-link--secondary">KKK</a>'
    )

    # 4. Toriistad toggle -> prominent
    content = content.replace(
        '<button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Tööriistad</button>',
        '<button class="nav-dropdown-toggle nav-dropdown-toggle--prominent" aria-expanded="false" aria-haspopup="true">Tööriistad</button>'
    )

    # 5. CTA button text
    content = content.replace('>Kontrollin valmisolekut<', '>Tee eneseanalüüs<')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def process_subdir_file(filepath):
    """Process a file in artiklid/ or linnad/ subdirectory."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Wrap nav-logo in nav-brand + add Meist link (relative path)
    old_logo = (
        '    <a href="../index.html" class="nav-logo" aria-label="TT24 avaleht">\n'
        '      <span class="nav-logo-text">TT24</span>'
        '<span class="nav-logo-tagline">Töötervishoiu Teejuht</span>\n'
        '    </a>'
    )
    new_logo = (
        '    <div class="nav-brand">\n'
        '      <a href="../index.html" class="nav-logo" aria-label="TT24 avaleht">\n'
        '        <span class="nav-logo-text">TT24</span>'
        '<span class="nav-logo-tagline">Töötervishoiu Teejuht</span>\n'
        '      </a>\n'
        '      <a href="../meist.html" class="nav-brand-meist">Meist</a>\n'
        '    </div>'
    )
    content = content.replace(old_logo, new_logo)

    # 2. Remove Meist from main nav (relative paths)
    content = content.replace(
        '\n      <a href="../meist.html" class="nav-link nav-link--secondary">Meist</a>',
        ''
    )
    content = content.replace(
        '\n      <a href="../meist.html" class="nav-link nav-link--secondary active">Meist</a>',
        ''
    )

    # 3. KKK -> secondary style (relative path)
    content = content.replace(
        '<a href="../korduma.html" class="nav-link">KKK</a>',
        '<a href="../korduma.html" class="nav-link nav-link--secondary">KKK</a>'
    )

    # 4. Toriistad toggle -> prominent
    content = content.replace(
        '<button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Tööriistad</button>',
        '<button class="nav-dropdown-toggle nav-dropdown-toggle--prominent" aria-expanded="false" aria-haspopup="true">Tööriistad</button>'
    )

    # 5. CTA button text
    content = content.replace('>Kontrollin valmisolekut<', '>Tee eneseanalüüs<')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def process_index_hero(filepath):
    """Extra changes only for index.html hero and urgency CTAs."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Hero primary CTA
    content = content.replace(
        '>Kontrollin oma valmisolekut \u2192<',
        '>Tee eneseanalüüs \u2192<'
    )
    # Urgency section CTA (has arrow too)
    content = content.replace(
        '>Kontrollin valmisolekut \u2192<',
        '>Alusta eneseanalüüsi \u2192<'
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


changed = []
unchanged = []

# Root-level HTML files
root_html = glob.glob(os.path.join(ROOT, '*.html'))
for fp in root_html:
    result = process_root_file(fp)
    if result:
        changed.append(fp)
    else:
        unchanged.append(fp)

# index.html hero special
idx = os.path.join(ROOT, 'index.html')
process_index_hero(idx)

# artiklid/ files
for fp in glob.glob(os.path.join(ROOT, 'artiklid', '*.html')):
    result = process_subdir_file(fp)
    if result:
        changed.append(fp)
    else:
        unchanged.append(fp)

# linnad/ files
for fp in glob.glob(os.path.join(ROOT, 'linnad', '*.html')):
    result = process_subdir_file(fp)
    if result:
        changed.append(fp)
    else:
        unchanged.append(fp)

print(f"Changed: {len(changed)} files")
for f in sorted(changed):
    print(f"  CHANGED: {os.path.relpath(f, ROOT)}")
print(f"Unchanged: {len(unchanged)} files")
for f in sorted(unchanged):
    print(f"  unchanged: {os.path.relpath(f, ROOT)}")
