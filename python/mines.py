import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
