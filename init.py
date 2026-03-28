import streamlit as st
import yaml
import os
import sys
from datetime import datetime

# 配置
CONTENT_DIR = "."

def get_writeable_dir():
    # 如果是打包后的环境
    if hasattr(sys, '_MEIPASS'):
        # sys.executable 是可执行文件所在的绝对路径
        # 我们取它的父目录，确保文件生成在 .exe/.app 旁边
        return os.path.dirname(sys.executable)
    # 如果是普通的 python 运行环境
    return os.path.abspath(".")

def save_markdown(category, filename, data):
    """通用保存函数"""
    dir_path = os.path.join(CONTENT_DIR, category)
    os.makedirs(dir_path, exist_ok=True)
    filepath = os.path.join(dir_path, f"{filename}.md")

    # 转换为 YAML Frontmatter
    frontmatter = yaml.dump(data, allow_unicode=True, sort_keys=False)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"---\n{frontmatter}---\n\n# {data.get('title', '')}\n\n在这里输入正文内容...")
    return filepath


# --- 页面布局 ---
st.set_page_config(page_title="Nuxt Content 管理器", layout="wide")
st.title("🚀 联协内容自动化生成器")
st.sidebar.title("选择内容类型")

menu = st.sidebar.selectbox(
    "你想发布什么？",
    ["活动 (Activities)", "官方博客 (Blog)", "官方公告 (Notice)", "官方进度 (Timeline)", "组织 (Orgs)",
     "联协公招 (Project)", "联协映像 (Archive)"]
)

# --- 逻辑处理 ---
with st.container():
    if menu == "活动 (Activities)":
        st.subheader("🆕 新增活动")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("活动标题")
            date = st.date_input("举办时间")
            status = st.selectbox("活动形式", ["online", "in_person", "regional"])
        with col2:
            org = st.text_input("所属组织代号 (如: NEXUS)")
            author = st.text_input("编写人")
            type_val = st.selectbox("活动类型", ["Official", "Anniversary", "Nexus"])
        desc = st.text_area("简要介绍")

        if st.button("生成活动文件"):
            filename = f"{date}-{title.replace(' ', '-')}"
            data = {"title": title, "description": desc, "date": str(date), "status": status, "org": org,
                    "author": author, "type": type_val}
            path = save_markdown("activities", filename, data)
            st.success(f"文件已保存至: {path}")

    elif menu == "组织 (Orgs)":
        st.subheader("🏢 组织入驻")
        col1, col2, col3 = st.columns(3)
        with col1:
            org_id = st.text_input("组织 ID (文件名)", placeholder="nexus-lab")
            title = st.text_input("组织名称")
            leader = st.text_input("负责人")
        with col2:
            founded = st.date_input("成立时间")
            joined = st.date_input("加入联协时间")
            members = st.number_input("成员数量", min_value=1, value=1)
        with col3:
            location = st.selectbox("范围", ["Regional", "Global"])
            org_type = st.selectbox("类型", ["FC", "DKK"])
            tag = st.selectbox("标签", ["Branch", "Official"])

        st.markdown("---")
        st.write("🎨 主题配置")
        c1, c2, c3 = st.columns(3)
        logo = c1.text_input("Logo (Lucide 或 URL)", "lucide:shrub")
        color = c2.color_picker("主题色", "#7c3aed")
        bg = c3.text_input("背景图路径", "/orgs/test.jpg")

        desc = st.text_area("组织介绍")

        if st.button("生成组织档案"):
            data = {
                "orgs_id": org_id, "title": title, "description": desc, "founded": str(founded),
                "joined_at": str(joined), "members_count": members, "status": True,
                "leader": leader, "location": location, "type": org_type, "tag": tag,
                "theme": {"logo": logo, "primaryColor": color, "bgImage": bg}
            }
            save_markdown("orgs", org_id, data)
            st.success("组织文件已创建！")

    elif menu == "联协公招 (Project)":
        st.subheader("📢 发布公招")
        title = st.text_input("项目名称")
        desc = st.text_area("项目介绍")
        col1, col2 = st.columns(2)
        with col1:
            org = st.text_input("所属组织")
            status = st.selectbox("招募状态", ["funding", "need_creator", "finding_resonance", "others"])
        with col2:
            author = st.text_input("发布人")
            link = st.text_input("组织链接")

        if st.button("生成公招"):
            filename = f"project-{datetime.now().strftime('%m%d%H%M')}"
            data = {"title": title, "description": desc, "orgs": org, "date": datetime.now().strftime("%Y-%m-%d"),
                    "author": author, "status": status, "link": link}
            save_markdown("projects", filename, data)
            st.success("公招信息已发布至 Content")
    elif menu == "活动 (Activities)":
        st.subheader("📅 新增活动")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("活动标题")
            date = st.date_input("举办时间")
            status = st.selectbox("活动形式", ["online", "in_person", "regional"])
        with col2:
            org = st.text_input("所属组织 (英文代号)")
            author = st.text_input("编写人")
            type_val = st.selectbox("类型", ["Official", "Anniversary", "Nexus"])
        desc = st.text_area("活动简要介绍")

        if st.button("生成活动 Markdown"):
            data = {"title": title, "description": desc, "date": str(date), "status": status, "org": org,
                    "author": author, "type": type_val}
            path = save_markdown("activities", f"{date}-{title}", data)
            st.success(f"已生成: {path}")

        # 2. 官方博客 (Blog)
    elif menu == "官方博客 (Blog)":
        st.subheader("✍️ 撰写博客")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("文章标题")
            author = st.text_input("作者")
        with col2:
            date = st.date_input("发布时间")
            type_val = st.selectbox("文章类型", ["docu", "artic", "rese"])  # 文件, 推文, 研究成果
        desc = st.text_area("博客摘要")

        if st.button("生成博客"):
            data = {"title": title, "date": str(date), "description": desc, "author": author, "type": type_val}
            save_markdown("blog", f"blog-{date}-{title}", data)
            st.success("博客文件已创建")

        # 3. 官方公告 (Notice)
    elif menu == "官方公告 (Notice)":
        st.subheader("📢 发布官方公告")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("公告标题")
            author = st.text_input("发布人")
        with col2:
            date = st.date_input("发布时间")
            type_val = st.selectbox("公告性质", ["regula", "event", "notice"])  # 条例, 活动, 公告
        desc = st.text_area("公告内容简述")

        if st.button("生成公告"):
            data = {"title": title, "date": str(date), "description": desc, "author": author, "type": type_val}
            save_markdown("notice", f"notice-{date}", data)
            st.success("公告已存档")

        # 4. 官方进度 (Timeline)
    elif menu == "官方进度 (Timeline)":
        st.subheader("⏳ 项目进度记录")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("事项标题")
            author = st.text_input("记录人")
        with col2:
            date = st.date_input("记录时间")
            status = st.selectbox("进度状态", ["Prog", "Changes", "Record"])  # 进度, 更改, 记录
        desc = st.text_area("详细进展描述")

        if st.button("更新时间轴"):
            data = {"title": title, "date": str(date), "description": desc, "author": author, "status": status}
            save_markdown("timeline", f"timeline-{date}", data)
            st.info("时间轴已更新")

        # 5. 组织 (Orgs) - 包含嵌套主题
    elif menu == "组织 (Orgs)":
        st.subheader("🏢 组织管理")
        col1, col2, col3 = st.columns(3)
        with col1:
            org_id = st.text_input("组织唯一 ID", placeholder="nexus-lab")
            title = st.text_input("组织名称")
            leader = st.text_input("负责人")
        with col2:
            founded = st.date_input("成立时间")
            joined = st.date_input("加入时间")
            members = st.number_input("成员数", min_value=0)
        with col3:
            location = st.selectbox("范围", ["Regional", "Global"])
            org_type = st.selectbox("组织类型", ["FC", "DKK"])
            tag = st.selectbox("标签", ["Branch", "Official"])

        st.write("🎨 UI 主题定制")
        c1, c2, c3 = st.columns(3)
        logo = c1.text_input("Icon", "lucide:shrub")
        color = c2.color_picker("主题色", "#7c3aed")
        bg = c3.text_input("背景图 URL", "/orgs/test.jpg")

        desc = st.text_area("组织简介")

        if st.button("生成组织档案"):
            data = {
                "orgs_id": org_id, "title": title, "description": desc, "founded": str(founded),
                "joined_at": str(joined), "members_count": members, "status": True,
                "leader": leader, "location": location, "type": org_type, "tag": tag,
                "theme": {"logo": logo, "primaryColor": color, "bgImage": bg}
            }
            save_markdown("orgs", org_id, data)
            st.success(f"组织 {title} 已入驻")

        # 6. 联协公招 (Project)
    elif menu == "联协公招 (Project)":
        st.subheader("🤝 公开招募项目")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("项目名称")
            org = st.text_input("所属组织")
            status = st.selectbox("要求类型", ["funding", "need_creator", "finding_resonance", "others"])
        with col2:
            author = st.text_input("发布人")
            link = st.text_input("链接 (URL)")
            date = st.date_input("发布日期")
        desc = st.text_area("招募详细要求")

        if st.button("发布公招"):
            data = {"title": title, "description": desc, "orgs": org, "date": str(date), "author": author,
                    "status": status, "link": link}
            save_markdown("projects", f"proj-{title}", data)
            st.success("公招已发布")

        # 7. 联协映像 (Archive)
    elif menu == "联协映像 (Archive)":
        st.subheader("🖼 内容映像存档")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("映像名称")
            org = st.text_input("所属组织")
        with col2:
            date = st.date_input("日期")
            archive_type = st.selectbox("媒体类型", ["Gallery", "tweet"])
        author = st.text_input("上传/记录人")
        desc = st.text_area("映像背景介绍")

        if st.button("保存映像"):
            data = {"title": title, "description": desc, "orgs": org, "date": str(date), "author": author,
                    "type": archive_type}
            save_markdown("archive", f"arc-{title}", data)
            st.success("映像已归档")
    else:
        st.info(f"【{menu}】的表单逻辑已就绪，可根据需要快速克隆上述代码实现。")