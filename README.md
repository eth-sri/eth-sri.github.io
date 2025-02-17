# SRI Website

## Notice

All larger files, including pdfs of papers/slides, should be uploaded to the file server.

```
$ ssh websrl@web-login-el6.inf.ethz.ch
[websrl@web-login htdocs-srl]$ cd /import/vechev/h1/htdocs-srl/website
```
Upload you files to the '/import/vechev/h1/htdocs-srl/website' directory. All files are then available under https://files.sri.inf.ethz.ch/ url. For example, file in '/import/vechev/h1/htdocs-srl/website/slides/deguard-androidsec17.pdf' is available at https://files.sri.inf.ethz.ch/website/slides/deguard-androidsec17.pdf

## Overview

The site is built on [Jekyll](https://jekyllrb.com/), a static site generator. The templating language is [Liquid](https://shopify.github.io/liquid/). 

To serve the webpage locally, run `jekyll serve`.
You may need to run `bundle install` in case of errors like `Could not find gem`.

## Installation

Installation is not required when editing directly on GitHub. To setup on your local machine, follow the [Jekyll docs](https://jekyllrb.com/docs/)


## Making Updates
After a commit, GitHub should re-generate the site (usually in under a minute, but it may take up to 5 minutes). 

To automatically normalize used room names and wrap them into a link pointing to the roomfinder, run [`python clean_rooms_add_links.py`].

## Types of Content
The types of content on the site:

- People 
- Blog Posts
- News Posts
- Media (News with photos)
- Research Projects
- Publications 
- Teaching (Courses)
- Events (Workshop series)

## Storage areas
The main folder for storage is `/assets`. It contains stock icons, logos and images from the old site. However, some types of content have their own corresponding storage area, usually at the root level of the site. This includes the following folders:


*  `/people`: stores each lab member's individual files

All other types of resources such as publication pdfs, slides, teaching materials should be uploaded on the file server in '/import/vechev/h1/htdocs-srl/website' 


## General Editing

### Front matter
At the top of each content file is the front matter, which is YAML style data storage. This data can be used by layout files, or be used to search and filter files by. Here is an example of front matter.

```yaml
---
layout: newspost
date:   2012-06-01
category: news
---
``` 

Unfortunately, YAML cannot parse certain characters, such as the colon (:). If the title of your publication has a colon in it, wrap your title in a set of quotation marks.

```yaml
---
title: "Artificial Intelligence: A Modern Approach"
---
```

### Layouts
You can change the layout of a file by specifying it in the front matter. A number of layouts are available, such as the ones made specifically for `publication`, `person`, `project`, `course`, and `event`. The standard layout is `page`, which can be used if you want to add a file outside of the content types specified above.

```yaml
---
layout: page
---
```

### The content itself
You can write any valid HTML or Markdown after the front matter, but you cannot mix the two in the same file. You can insert tables, images, etc. Avoid writing custom CSS; try to re-use CSS classes and images from other finished content.


## Editing/Adding Content for Specific Content Types

### Home Page
To edit the homepage 'about' text, go to \_layouts/home.html.
Adding or editing news items will automatically re-populate the news feed on the homepage.
Adding or editing media items will also automatically re-populate the 'In the Media' section on the homepage.

### People
Where to edit: `\_people`
Storage area: `\people`

#### Personal Info section
Your email, office, website, phone number, and CV only appear on your page if it is filled in the front matter of your html file.

Your CV should be in PDF format. It can be either:
1. Uploaded to an external site. You can then provide an URL in the CV field.
2. Uploaded to this site. In the `\people` folder, create a folder with your first name (if it's not already there), and upload your CV to it. Then fill in the following path for the CV field (where your name is Jimmy):

```yaml
---
cv: jimmy/cv.pdf
---
```

#### Publications section
If you want to automatically populate your publications by pulling from the existing lab publications, use this code (where your name is Jimmy):

```
{% include get-publications.html filter="person" key="Jimmy" %}
```

You can also pull in one publication at a time (where the `ref` of your publication is arnold2011qvm):

```
{% include get-publications.html filter="id" key="arnold2011qvm" %}
```

#### Other sections
You can put in any other sections you want on your personal page! Use h2 for each section heading.

If you would like to upload and display any personal files on your page, remember to upload them to your personal folder in the `\people`.


#### Pulling 'person' info in other pages
You can include the information of a lab member on a particular page. Pull them in using the following code:

```
{% include get-person.html title="Jimmy Foo" %}
```


### Publications
Where to edit: `\_publications`\
Storage areas: `/import/vechev/h1/htdocs-srl/website/papers`, `/import/vechev/h1/htdocs-srl/website/slides`, `/import/vechev/h1/htdocs-srl/website/posters`
Make sure to keep slides and posters properly placed.

The main publications list (publications.html) contains all papers authored by Martin.

You may create files under `\_publications` for your own papers. 

To create a new publication:
1. Create a reference name (e.g., jimmy2019ai). Use the same reference name in the html filename (e.g., jimmy2019ai.html), and for the 'ref' field in the front matter of the html file. 
2. Upload the publication on the file server and specify the full url as 'paper' field. 
If your publication is already uploaded to an external site, simply provide the URL for the 'paper' field.
3. A talk is a recorded presentation for your publication, and it's always assumed to have been uploaded to an external site (e.g. Youtube). Provide its URL in the 'talk' field in the front matter of the html file. 
4.  If you have presentation slides for your publication, upload them on the file server and specify 'slides' field with their url. 


```yaml
---
ref: jimmy2019ai
paper: jim_pub2019.pdf
talk: https://www.youtube.com/watch?v=AWh9gESAOO0
slides: jim_present2019.pdf
---
```

#### Pulling publications in by name
If you would like to automatically pull in your own papers (e.g., to display on your personal page), use the following code:

```
{% include get-publications.html filter="person" key="Jimmy" %}
```

#### Pulling publications in by reference
To pull in publications one at a time, use the following code:

```
{% include get-publications.html filter="id" key="arnold2011qvm" %}
```

#### Pulling publications in by project
To specify a publication as belonging to a particular research project, add the appropriate reference name of the research project into the publication's front matter. For example:

```yaml
projects: plml
```
Then, you can use the following code to pull in the publications for a particular project:

```
{% include get-publications.html filter="project" key="plml" %}
```

You can tag multiple research projects into a single publication.

See the [Research Projects](#research-projects) section for existing project reference names.


### Blog Posts
Where to edit: `\_blogposts`

To add a blog post follow the [Guidelines Doc](https://docs.google.com/document/d/1Gk5bx133f0bnjzbS7PiUMOj-6fhAGP8lV6ZPUL2S1yo/edit?usp=sharing).

### News
Where to edit: `\_newsposts`

To add a news item, simply add it as a file in the `\_newsposts` folder. Make sure to name the file to include the appropriate date, so that the item appears in the right spot on the news feed.


### Media

Where to edit: `\_media`

To add a news item that appears in the 'In the Media' section of the homepage, simply add it as a file in the `\_media` folder. There should be an image that accompanies the news item. Add the image to the `\assets\media` folder and specify its file name in the front matter of the news file.


### Research Projects
Where to edit: `\_projects`\
Storage areas: `\assets\projects`, `\assets\systems`

To create a new project, assign it a reference name by specifying it in the front matter of the project page.

Currently, there are reference names for the following projects:

| Project                                                                    | Reference name           |
| ----------------------------------------------------------------- | -------------------------------- |
| Safe and Interpretable Artificial Intelligence     | safeai  |
| Machine Learning for Programming   | plml     |
| Probabilistic Programming and Applications     | probabilistic-programming   |
| Programmable Networks     | programmable-networks   |
| Blockchain Security       | blockchain-security      |
| Fast Numerical Abstract Domains     | numerical-analysis    |
| Computational Biology               | computational-biology |

You can create a number of sections to showcase various aspects of the project, such as associated startups, systems, publications and talks. 

You can use 'cards' to display parts of your project. There are vertical cards and horizontal cards. Vertical cards are mostly used to display logos, descriptions, and to provide a link to an external site. Horizontal cards are mostly used to provide information and download links for materials relevant to the project (e.g., publications, slides, and data sets. See existing project files for examples.

As always, tagged publication can automatically be pulled in using the following code:

```
{% include get-publications.html filter="project" key="plml" %}
```

You can also pull in information about a research project on any page by using the following code:

```
{% include get-project.html ref="safeai" %}
```

You can change the output style:

```
{% include get-project.html ref=page.projects output="plain" %}
```


### Teaching
Where to edit: `\_teaching`\
Storage areas: `/import/vechev/h1/htdocs-srl/website/teaching`

Courses are listed on the teaching.html page, and are pulled in one by one:

```
{% include get-course.html ref="riai2018"  output="horizontal" %}
```
To create a new course, assign it a reference name (e.g., pa2019) . Use the same reference name in the html filename (e.g., pa2019.html), in the front matter within the html file (`ref: pa2019`), and in the storage folder name in `\teaching`. 

When creating download links to your teaching materials, use the appropriate icons.

| Icon       | Path                | Used for     |
| ------------- | ------------------ | ----------------- |
| slides | /assets/icons/icon-slides.svg  | Presentation slides   |
| pdf | /assets/icons/icon-pdf.svg      | PDF files that aren't slides (papers, exercises, solutions)   |
| download | /assets/icons/icon-download.svg   | Other file types (zip, tar, 7z, psi, etc.)

Remember to specify the proper "alt" tag for your file.


#### Events
Where to edit: `\_events`\
Storage areas: `/import/vechev/h1/htdocs-srl/website/events`

Events are special in that they do not contain the main menu of the site. 

Each event can have a background image.

Currently the Events section is used for workshops.



