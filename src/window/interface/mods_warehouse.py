# Licensed under the GNU General Public License v3.0, see <http://www.gnu.org/licenses/gpl-3.0.html>.
# d3dxSkinManage Copyright (C) 2023 numlinka.

# std
import os
import webbrowser

# site
import ttkbootstrap

# self
import core
from constant import *


MW_INFO = "该功能已被禁用，这东西没啥用，你也用不到，所以禁用\n不影响其它功能，别像一个呆子似的不看公告在这儿瞎问"


class ModsWarehouse(object):
    def install(self, master, *args, **kwds):
        self.master = master
        self.disabled = ttkbootstrap.Label(self.master, text=MW_INFO, anchor="center")
        self.disabled.pack(fill="both", expand=True)
        return
        titles = (("#0", "object / name", 360), ("enabled", "tags", 480))

        self.value_entry_search = ttkbootstrap.StringVar()

        self.Frame_list = ttkbootstrap.Frame(self.master)
        self.Frame_list.pack(side="left", fill="y")

        self.Entry_search = ttkbootstrap.Entry(self.Frame_list, textvariable=self.value_entry_search)
        self.Treeview_items = ttkbootstrap.Treeview(self.Frame_list, show="tree headings", selectmode="extended", columns=("enabled",))
        self.Scrollbar_items = ttkbootstrap.Scrollbar(self.Frame_list, command=self.Treeview_items.yview)
        self.Frame_Button = ttkbootstrap.Frame(self.master)
        self.Button_download = ttkbootstrap.Button(self.Frame_Button, text="添加到下载列表", width=10, bootstyle="outline", command=self.bin_download)
        self.Button_open_url = ttkbootstrap.Button(self.Frame_Button, text="在浏览器上查看", width=10, bootstyle="outline", command=self.bin_open_url)
        self.Label_preview = ttkbootstrap.Label(self.master, anchor="center", text="无预览图")

        self.Entry_search.pack(side="bottom", fill="x", padx=10, pady=10)
        self.Scrollbar_items.pack(side="right", fill="y", padx=(0, 10), pady=(10, 0))
        self.Treeview_items.pack(side="left", fill="y", padx=(10, 5), pady=(10, 0))
        self.Frame_Button.pack(side="bottom", fill="x", padx=(0, 10), pady=10)
        self.Button_download.pack(side="left", fill="x", expand=1, padx=0, pady=0)
        self.Button_open_url.pack(side="right", fill="x", expand=1, padx=(10, 0), pady=0)
        self.Label_preview.pack(side="top", fill="both", padx=(0, 10), pady=(10, 0), expand=1)


        self.Treeview_items.config()
        self.Treeview_items.config(yscrollcommand=self.Scrollbar_items.set)

        self.Treeview_items.bind("<<TreeviewSelect>>", self.bin_items_TreeviewSelect)
        self.Treeview_items.bind("<Double-1>", self.bin_download)
        # self.Entry_search.bind("<Return>", self.refresh)
        self.value_entry_search.trace("w", self.refresh)
        # self.Entry_search.bind("<Key>", self.bin_refresh)
        for tree, text, width in titles:
            self.Treeview_items.column(tree, width=width, anchor="w")
            self.Treeview_items.heading(tree, text=text)


    def initial(self):
        return
        _alt_set = core.window.annotation_toplevel.register

        _alt_set(self.Entry_search, T.ANNOTATION_WAREHOUSE_SEARCH, 1)
        _alt_set(self.Button_download, T.ANNOTATION_WAREHOUSE_DOWNLOAD, 2)
        _alt_set(self.Button_open_url, T.ANNOTATION_WAREHOUSE_OPEN_URL, 2)


    def __init__(self, master):
        self.master = master
        self.install(master)


    def refresh(self, *_):
        return
        core.log.debug("更新 Mods 列表", L.WINDOS_MODS_WAREHOUSE)

        search = self.value_entry_search.get()
        all_list = core.module.mods_index.get_all_sha_list()
        exist_list = self.Treeview_items.get_children()
        to_list = []
        to_data = {}

        for SHA in all_list:
            item = core.module.mods_index.get_item(SHA)
            if not item.get(K.INDEX.GET, None): continue
            if not core.module.extension.item_dict_conform(SHA, item, search): continue
            to_list.append(SHA)
            to_data[SHA] = item

        # 剔除已经不存在的分类
        nonexistent = set(exist_list) - set(to_list)
        self.Treeview_items.delete(*nonexistent)

        for index, SHA in enumerate(to_list):
            try:
                item = to_data[SHA]
                object_ = item[K.INDEX.OBJECT]
                name = item[K.INDEX.NAME]
                grading = item.get(K.INDEX.GRADING, "X")
                author = item.get(K.INDEX.AUTHOR, "-")
                author = "-" if not author else author
                tags = " ".join(item.get(K.INDEX.TAGS, []))
                local_ = core.module.mods_manage.is_local_sha(SHA)

                islocal = " [已下载]" if local_ else ""
                isdownloading = " [正在下载...]" if core.module.mod_download.is_downloading(SHA) else ""

                text = f"{object_}\n{name}"
                values = (f"{author} {tags}\n[{grading}]{islocal}{isdownloading}", )

                image = core.window.treeview_thumbnail.get(object_)

                if SHA in exist_list:
                    self.Treeview_items.item(SHA, text=text, values=values, image=image, tags=(SHA, ))

                else:
                    self.Treeview_items.insert("", index, SHA, text=text, values=values, image=image, tags=(SHA, ))

            except Exception:
                ...


    def sbin_update_preview(self, SHA: str | None = None):
        return
        if SHA is None:
            self.Label_preview.config(image="")
            self.Label_preview.config(text="无预览图")
            return
        width = self.Label_preview.winfo_width()
        height = self.Label_preview.winfo_height()
        self.__image = core.module.image.get_preview_image(SHA, width, height)
        if self.__image is None: self.sbin_update_preview(None)
        else: self.Label_preview.config(image=self.__image)


    def bin_items_TreeviewSelect(self, *args):
        return
        SHA = self.Treeview_items.focus()
        SHA = SHA if SHA else None
        self.sbin_update_preview(SHA)


    def bin_download(self, *args, **kwds):
        return
        tags = self.Treeview_items.item(self.Treeview_items.focus())["tags"]
        if not tags: SHA = None
        else: SHA = tags[0]
        if SHA == None:
            core.window.messagebox.showerror(title="数据错误", message="数据值为空\n请先选择需要下载的 Mod")
            return
        else:
            core.construct.taskpool.newtask(core.module.mod_download.download_task, (SHA, ))


    def bin_open_url(self, *args, **kwds):
        return
        tags = self.Treeview_items.item(self.Treeview_items.focus())["tags"]
        if not tags: SHA = None
        else: SHA = tags[0]
        if SHA == None:
            core.window.messagebox.showerror(title="数据错误", message="数据值为空\n请先选择需要下载的 Mod")
            return
        else:
            item = core.module.mods_index.get_item(SHA)
            webbrowser.open(item["get"][0]["url"])


    def bin_refresh(self, *args, **kwds):
        return
        key = self.Entry_search.get()
        self.refresh(key)

