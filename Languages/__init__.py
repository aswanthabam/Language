import re 
class HyperTextMarkup:
    html = None
    Doctype = None
    Head = None
    Body = None
    tags = None
    selfClosing = None
    closingTags = None
    AllTagData = None
    removeAllTags = None
    link = None
    meta = None
    style = None
    script = None
    RequestedTag = None
    Data = None
    contents = None
    NoOfTags = None
    attributes = None
    loop = None
    getedData = None
    Comments = None
    findAllData = None
    OriginalData = None
    def __init__(self,data):
        try:
            data = open(data,"r").read()
            self.OriginalData = data
        except:
            data = data
            self.OriginalData = data
        data = data.replace("\n","")
        tags1 = re.findall("<.*?>",data)
        tags = []
        self.Comments = []
        self.html = data
        for x in tags1:
            if "!doctype html" in x.lower():
                self.Doctype = x
                continue
            if "<!--" in x:
                self.Comments.append(x)
                continue
            tags.append(x)
            if "<head" in x:
                head = re.findall(f"{x}(.*?)</head>",data)
                self.Head = head[0]
                continue
            if "<body" in x:
                body = re.findall(f"{x}(.*)</body>",data)
                self.Body = body[0]
                continue
            continue
        self.tags = tags
        self.selfClosing = []
        tag = []
        self.closingTags = []
        self.AllTagData = {}
        mg = []
        var2 = re.compile(r"<[^>]+>")
        self.removeAllTags = var2.sub("",data)
        for x in tags:
            if "</" not in x and "/" in x:
                self.selfClosing.append(x)
                continue
            if "</" in x:
                self.closingTags.append(x)
                continue
            if " " in x:
                attributes = []
                try:
                    var4 = x.split(" ")
                    i = 0
                    for y in var4:
                        i = i + 1
                        if i == 1:continue
                        var3 = y.replace(">","").replace(">","").split("=")
                        attributes.append((var3[0],var3[1]))
                except:
                    attributes = []
                x = x.split(" ")[0]+">"
            else:
                attributes = []
            if x.replace(">","").replace("<","") in mg:
                vr = self.AllTagData[x.replace("<","").replace(">","")]["attributes"]
                lst = [y for y in vr.items()]
                last = lst[len(lst)-1][0] + 1
                mrr = {last:attributes}
                vr.update(mrr)
                continue
            tag.append(x)
            contents = re.findall(f'<{x.split(" ")[0].replace(">","").replace("<","")}.*?>(.*?){x.replace("<","</")}',data)
            mg.append(x.replace("<","").replace(">","").split(" ")[0])
            formated = {x.replace("<","").replace(">",""):{"contents":contents,"TotalNumberOfTags":len(contents),"attributes":{1:attributes}}}
            self.AllTagData.update(formated)
        mg = []
        for x in self.selfClosing:
            if " " in x:
                tag = x.split(" ")[0].replace("<","").replace(">","").replace("/","")
            else:
                tag = x.replace(">","").replace("<","").replace("/","")
            attributes = []
            if " " in x:
                var1 = x.split(" ")
                try:
                    for y in var1[1:]:
                        try:
                            var2 = y.split("=")
                        except:
                            var2 = None
                        attr = var2[0]
                        try:
                            val = var2[1].replace(">","").replace("/","")
                        except:
                            val = None
                        attributes.append((attr,val))
                except:
                    attributes = []
            contents = None
            if tag in mg:
                var3 = self.AllTagData[tag]["attributes"]
                var4 = [g for g in var3]
                last = var4[len(var4)-1] + 1
                ff = {last:attributes}
                var3.update(ff)
                continue
            the_all_tag = re.findall(f"<{tag}.*?/>",data)
            fff = {tag:{"contents":contents,"TotalNumberOfTags":len(the_all_tag),"attributes":{1:attributes}}}
            self.AllTagData.update(fff)
            mg.append(tag)
        self.link = []
        self.meta = []
        for x in self.selfClosing:
            if "<link" in x:
                self.link.append(x)
                continue
            if "<meta" in x:
                self.meta.append(x)
                continue
            continue
        self.style = []
        self.script = []
        for x in self.tags:
            if "<style" in x:
                self.style = self.style+re.findall(f"{x}.*?</style>",data)
                continue
            if "<script" in x:
                self.script = self.script+re.findall(f"{x}.*?</script>",data)
        return None
    def get(self,tag):
        i = 0
        for x in self.tags:
            i = i +1
            if tag in x:
                break
            else:
                if i == len(self.tags):
                    print(f'HyperTextMarkup Traceback:\nerror in object.get("{tag}").\nNo tag named {tag}')
                    quit()
                continue
        self.RequestedTag = tag
        self.Data = self.AllTagData[tag]
        self.contents = self.Data["contents"]
        self.NoOfTags = self.Data["TotalNumberOfTags"]
        self.attributes = self.Data["attributes"]
        self.loop = []
        i = 0
        for x in self.contents:
            i = i + 1
            formated = {"content":x,"attribute":self.attributes[i],"Num":i}
            self.loop.append(formated)
            continue
        lst = []
        for x in self.tags:
            if "</" in x:
                continue
            if " " in x:
                m = x.split(" ")[0] + ">"
            else:
                m = x
            if m.replace("<","").replace(">","") == tag:
                lst.append(x)
                continue
            continue
        self.getedData = lst
        return self.getedData
    def content(self,no):
        return self.contents[no]
    def attribute(self,no):
        return self.attributes[no]
    def find(self,data1):
        f = self.html.find(data1)
        self.findAllData = []
        if "\n" in self.OriginalData:
            lines = self.OriginalData.split("\n")
        else:
            lines = [self.OriginalData]
        for x in lines:
            if data1 in x:
                ind = lines.index(x)+1
                self.findAllData.append({"line":ind,"line-content":x})
                continue
            continue
class styleSheet:
    OriginalData = None
    selector = None
    AllData = None
    Format = None
    RequestedSelector = None
    RequestedData = None
    Type = None
    List = None
    def __init__(self,data):
        try:
            data = open(data,"r").read().replace("\n","")
            self.OriginalData = data
        except:
            data = data.replace("\n","")
            self.OriginalData = data
        data = data.replace("\n","")
        if "<style" in data:
            print("styleSheet Traceback:\nplease remove the style tag and give it")
            quit()
        self.selector = []
        mr = re.findall("(.*?){",data)
        for x in mr:
            if "}" in x:
                m = x.split("}")[1]
                self.selector.append(m)
                continue
            self.selector.append(x)
            continue
        self.AllData = {}
        for x in self.selector:
            state = x+"{(.*?)}"
            var1 = re.findall(state, data)
            for z in var1:
                if not ";" in z or not ":" in z:continue
                #print(z)
                for y in z.split(";"):
                    #print(y)
                    try:
                        var2 = y.split(":")
                        connector = var2[0].replace(" ","")
                        value = var2[1]
                    except:
                        continue
                    formated1 = {connector:value}
                    try:
                        self.AllData[x].update(formated1)
                    except:
                        self.AllData.update({x:formated1})
                    continue
                continue
            continue
        self.Format = ""
        for x in self.AllData.items():
            state = x[0] + "{\n"
            for y in x[1].items():
                state = state + "    " + y[0] + ": " + y[1] + ";\n"
                continue
            state = state + "}"
            self.Format = self.Format + "\n" + state
            continue
    def get(self,tag):
        self.RequestedSelector = tag
        try:
            data = self.AllData[tag]
            self.RequestedData = data
        except:
            print(f"styleSheet Traceback:\nNo selector {tag} this will make error in the future")
        if tag[0] == "#":
            self.Type = "Id"
        elif tag[0] == ".":
            self.Type = "Class"
        else:
            self.Type = "Tag"
        self.List = [x for x in data.items()]
    def remove(self,data):
        state = self.RequestedSelector + "{\n"
        for x in self.list:
            if x[0] == data:
                continue
            if x[0] == None:
                continue
            state = state + "    " + x[0] + ": " + x[1] + ";\n"
            continue
        state = state + "}"
        return state