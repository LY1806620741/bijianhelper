import os,sys,psutil

"""判断是否gui启动"""
def is_gui_win():
	image_name = 'explorer.exe'
	s = psutil.Process().parent()
	if s.name() == image_name or s.parent().name() == image_name:
		return True
	return False

if __name__ == '__main__':

    # 判断环境，选择模式
    if os.path.splitext(__file__)[-1] == ".pyw":
        # gui 模式
        import gui
        gui.Run(sys.arg)
    else:
        # 判断系统
        if sys.platform == "windows" and is_gui_win():
            pass
        else:
            # shell 模式
            import shell
            shell.Run(sys.argv)