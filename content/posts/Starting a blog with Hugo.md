---
title: Starting a blog with Hugo
date: 2024-12-06
draft: "false"
tags:
---


first download git and go and python

firstly create a folder in the obsidian vault with the name of posts
!![Image Description](/images/Pasted%20image%2020241206142134.png)

install hugo and add it to the env var 

```powershell
## Verify Hugo works
hugo version

## Create a new site 

hugo new site websitename
cd websitename

```

after this you have to initialize a git repo
```powershell
git init
```


now download a hugo theme from here [https://themes.gohugo.io/](https://themes.gohugo.io/)

I have choose this one https://gitlab.com/gabmus/hugo-ficurinia


now you have to add this theme to the hugo website with this command

```powershell
git submodule add -f [the repo link of the theme] themes/[name of the theme]
```

- Most themes you download will have an example configuration you can use. This is usually the best way to make sure Hugo works well and out of the box.
- For the _hugo-ficurinia_ theme, they gave this example config below.
```toml
baseURL = "https://example.com/"
theme = "hugo-ficurinia"
title = "My nice blog"
languageCode = "en"
defaultContentLanguage = "en"
# this will be included in the footer after the current year the site is last
# built, followed by the (c) symbol
# you can use markdown inside this field
copyright = "Some copyright notice - [my license](https://example.com/license)"
paginate = 5  # number of articles per page in the index
summaryLength = 70  # number of words for article summaries
[params]
    author = "Gabriele Musco"
    description = "A description for my website"  # this will be added as metadata
    posts = "posts"  # content directory where to find home page posts; default searches in "posts" and "post"
    showPostsLink = true  # show or hide the link to the simple post list
    extraContentDirs = []  # other content directories to render similarly to the home page
    showcaseDir = "showcase"  # create a content directory that shows a special showcase section in the home page
    # shows a specified single page as a home page, instead of the traditional articles list
    # requires setting `homeSinglePage`
    # goes well with extraContentDirs
    showSinglePageAsHome = false
    homeSinglePage = "/home"
    # It's best to put these icons in the "static" folder of your site
    logo = "/logo.svg"
    favicon = "/favicon.png"  # 32x32
    faviconIco = "/favicon.ico"  # 32x32
    appletouch = "/apple-touch-icon.png"  # 180x180
    svgicon = "/logo.svg"
    icon512 = "/icon512.png"  # 512x512 png image
    logoRightOfTitle = false  # positions the logo to the right of the title; default: false
    showTags = true  # show the Tags menu item; default true
    showRss = true  # show the link for the RSS feed; default true
    imageInArticlePreview = false  # show images in article preview; default false
    fitImageInArticlePreview = false  # make article preview images fit the article preview instead of getting cropped
    articleSummary = true  # show a summary in article preview; default true
    
    fontFamily = "JetBrains Mono"  # changes the font, default "JetBrains Mono"
    titleFontFamily = "JetBrains Mono"  # font used for titles and headings
    monospaceFontFamily = "JetBrains Mono"  # changes the monospace font for code, default "JetBrains Mono"
    # multipliers applied to font sizes, useful for custom fonts that may be too big or too small
    titleFontSizeMultiplier = 1.0
    mainFontSizeMultiplier = 1.0
    monoFontSizeMultiplier = 1.0
    contentWidth = "1000px"  # maximum width of the site content, css syntax
    paperCards = false  # enable paper card style; default false
    buttonTags = false  # enable button tag style; default false
    tagsInArticlePreview = true  # enable tags list in the article preview card
    gridView = false  # show post list as a grid. goes well with paperCards
    bigArticleTitle = false  # makes the title in the single article view bigger
    navtype = "standard"  # changes the style of the pagination, available styles are: "standard", "circles"
    enableShadow = false  # shows a shadow around some elements
    menuStyle = "standard"  # changes the style of the main site navigation menu, available styles are: "standard", "buttons"
    inputStyle = "standard" # changes the style of inputs (like the searchbar), available styles are: "standard", "buttons"
    enableSearch = true  # enable search page
    searchbarEverywhere = true  # if the searchbar should be shown in every page; requires enableSearch
    searchMenuLink = false  # add a search link to the navigation menu; requires enableSearch
    mobileHamburgerNav = false  # alternative hamburger menu layout for the main nav menu when screen is small
    enableFeatured = false  # enable a particular view for articles marked as featured (featured: true in the article frontmatter)
    underlineTitleLinks = false  # show an underline also for links that are titles
    # enable comments support with commento using the script from your server
    commento = "https://example.com/js/commento.js"
    # enable comments support with cactus comments (cactus.chat)
    cactusCommentsSiteName = "example.com"
    cactusCommentsServerName = "cactus.chat"
    cactusCommentsHomeserver = "https://matrix.cactus.chat:8448"
    # enable analytics using Plausible
    plausibleScriptUrl = "https://something.com/..."
    plausibleDomain = "example.com"
    # enable analytics using Umami
    umamiScriptUrl = "https://something.com/..."
    umamiWebsiteId = "example-tracking-code"
    enableShareOnFediverse = false  # enable a button at the end of an article to share it on the fediverse
    tocBeforeImage = false  # show the table of contents before the main article image; default false
    # WARNING: deprecated! Use [[menu.icons]] instead, look below
    # links = [
    #     ["GitLab", "https://gitlab.com/gabmus"],
    #     ["GNOME", "https://gitlab.gnome.org/gabmus"],
    #     ["YouTube", "https://youtube.com/TechPillsNet"]
    # ]
    # you can customize all of the colors in this theme
    # Colors are defined in data/colors.yml
    # alternative sidebar layout
    enableSidebarLayout = false
    tocInSidebar = false  # if the sidebar is enbabled, show the TOC in the sidebar
    # redirect to baseURL if current URL host doesn't match
    # useful if deploying in gitlab pages with custom domain and don't want
    # the username.gitlab.io/website url to persist
    # this requires you to set baseURL (see above)
    forceRedirect = false
    infiniteScrolling = false  # activates infinite scrolling instead of regular pagination
                               # NOTE: you need to enable JSON output for this to work!
                               #       look at the [outputs] section below
    enableFooterColumns = false  # activates footer columns, as described below
    enableJumbotron = false  # enables jumbotron, as described below
    # related articles will be selected randomly based on tags and shown at
    # the bottom of the article, after the comments
    enableRelatedArticles = false
    relatedArticlesNum = 2  # how many related articles to show
    randomRelated = false  # sorts related articles in random order (randomized at built time)
[menu]
    # these links will be added to the main navigation menu, sorted by weight
    # other elements in this menu are added automatically from the "pages" folder
    # the folder it will look into can be customized with the pages variable
    # in params above
    [[menu.main]]
        identifier = "about"
        name = "About"
        url = "/about/"
        weight = 10
    # these links (menu.icons) will be added as icon links below the main nav
    [[menu.icons]]
        identifier = "gitlab"
        name = "GitLab"
        url = "https://gitlab.com/gabmus"
        weight = 10
    [[menu.icons]]
        identifier = "gnome"
        name = "GNOME GitLab"
        url = "https://gitlab.gnome.org/gabmus"
        weight = 20
# this section is necessary if you want infinite scrolling
# it allows to output the article list as paged JSON so that "pages" can be retrieved via javascript
[outputs]
    home = ["HTML", "JSON"]
```

now replace what is in the hugo.toml file with the text that the theme documentation
!![Image Description](/images/Pasted%20image%2020241206143800.png)

lests test if every thing is working and run the server locally
```pwershell
hugo server -t [themename]
```

it's working but there isn't any posts !![Image Description](/images/Pasted%20image%2020241206144110.png)

lest add some posts

go the content folder and create a new folder and name it posts
```powershell
cd content
mkdir posts
```

now we have to sync the note in the posts folder in your obisidian with the posts folder in the hugo folder 

with this command
```powershell 
robocopy sourcepath destination /mir
```
!![Image Description](/images/Pasted%20image%2020241206144306.png)

when starting a new post add theses on the top they are meta data for hugo 
```
---
title: blogtitle
date: 2024-11-06
draft: false
tags:
  - tag1
  - tag2
---
```


there is still a problem when i add an image in my post in obsidian it does not appear in the blog cuz the image source is only in obisidian we have to add the image to hugo with this python script
```python
import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\chuck\Documents\salamehBlog\content\posts"
attachments_dir = r"C:\Users\chuck\Documents\my_second_brain\neotokos\Attachments"
static_images_dir = r"C:\Users\chuck\Documents\salamehBlog\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

```
name the file images.py and save it in the root folder in hugo

run the script to add the images from your obsidian to the blog
```powershell
python images.py
```
!![Image Description](/images/Pasted%20image%2020241206145530.png)

now lets upload this code to github
create a new repo 

click on the plus icon
!![Image Description](/images/Pasted%20image%2020241206145729.png)
now click on New repository
!![Image Description](/images/Pasted%20image%2020241206145803.png)
now write a name for your repo I'll write salamehBlog 
and make the repo public
!![Image Description](/images/Pasted%20image%2020241206150019.png)
now scroll down and click on the create repo
!![Image Description](/images/Pasted%20image%2020241206150113.png)

after you cliock the button you'll go to a new page scroll down untill you see this 
!![Image Description](/images/Pasted%20image%2020241206150557.png)
copy the first line and past it in the terminal 
```powershell
git remote add origin https://github.com/abda-s/salamehBlog.git
```

now type in the terminal 
```
hugo
```
to make sure every mark down file is converted to html

now lets add every thing to the repo with:
```
git add .
```

now lets commit the changes
```
git commit -m "first commit"
```

now lets push every thing to github
```bash
git push -u origin master
```

```bash
git subtree split --prefix public -b gh-pages-deploy
git push origin gh-pages-deploy:gh-pages --force
git branch -D gh-pages-deploy
```
