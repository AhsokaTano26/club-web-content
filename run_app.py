import streamlit.web.cli as stcli
import os
import sys
import platform


def get_resource_path(relative_path):
    """获取 PyInstaller 运行时的临时解压路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def main():
    # 1. 动态定位被封装的 init.py
    init_script_path = get_resource_path("init.py")

    # 2. 检查脚本是否存在（防御性编程）
    if not os.path.exists(init_script_path):
        print(f"Error: Cannot find {init_script_path}")
        sys.exit(1)

    # 3. 构造 Streamlit 启动参数
    # --global.developmentMode=false 减少非必要日志
    # --server.headless=true 防止在服务器环境弹出报错
    args = [
        "streamlit",
        "run",
        init_script_path,
        "--global.developmentMode=false",
    ]

    # 4. 针对 macOS 的特殊处理
    # 有些 macOS 环境下需要强制指定运行模式
    if platform.system() == "Darwin":
        os.environ["STREAMLIT_SERVER_HEADLESS"] = "false"

    sys.argv = args
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()