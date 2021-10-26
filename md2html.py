import markdown
import os
import glob
from shutil import copytree


class Page:
    def __init__(self):
        self.data=[]
    
    def build_page(self,src,target):
        # for filename in glob.iglob(src + '**/**', recursive=True):
        #     # print(filename,type(filename))
        #     ofile=str(filename).replace(src,target,1)
        #     copy(filename,ofile)
            # print(ofile)
        copytree(src,target,dirs_exist_ok=True)
        for filename in glob.iglob(src+'**/*.md',recursive=True):
            print(filename)
            with open(filename, 'r') as f:
                text = f.read()
                html = markdown.markdown(text, extensions=['codehilite','fenced_code'])
            outHtmlFile=str(filename).replace(src,target,1)
            outHtmlFile=str(outHtmlFile).replace('.md','.html',1)
            print(filename,"-",outHtmlFile)
            with open(outHtmlFile,'w') as f:
                f.write(html)          
            
        return True


page = Page()
page.build_page('./src/', './target/')