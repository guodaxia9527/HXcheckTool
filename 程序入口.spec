# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['程序入口.py'],
             pathex=['D:\\untitled1'],
             binaries=[
			 ('./img/button-alert.png','img'),
			 ('./img/info.png','img'),
			 ('./img/校对2.png','img'),
			 ],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='程序入口',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='16.ico')
