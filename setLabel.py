from xattr import xattr

def set_label(filename, color_name):
    colors = ['none', 'gray', 'green', 'purple', 'blue', 'yellow', 'red', 'orange']
    key = u'com.apple.FinderInfo'
    attrs = xattr(filename)
    current = attrs.copy().get(key, chr(0)*32)
    changed = current[:9] + chr(colors.index(color_name)*2) + current[10:]
    attrs.set(key, changed)

def get_label(filename):
	colors = ['none', 'gray', 'green', 'purple', 'blue', 'yellow', 'red', 'orange']

	attrs = xattr(filename)
	try:
		finder_attrs = attrs[u'com.apple.FinderInfo']
		flags = unpack(32*'B', finder_attrs)
		color = flags[9] >> 1 & 7
	except KeyError:
		color = 0
	return colors[color]
