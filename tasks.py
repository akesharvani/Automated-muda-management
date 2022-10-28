from RPA.Browser.Selenium import Selenium
from RPA.Word.Application import Application
import time 
import requests

browser = Selenium()

def open_word_doc():
    # Opening word document
    application = Application()
    application.open_application()
    application.open_file("blogs_updated.docx") 

    data = application.get_all_texts()

    application.close_document()

    # Seperating the blogs
    blogs = data.split("EOB")
    title = []
    content = []
    for blog in blogs:
        # Seperating the title and content
        title.append(blog.split("EOT")[0])
        content.append(blog.split("EOT")[1])
    
    return title, content

def automate_via_gui():
    # Ip of admin panel muda management
    ip = "http://127.0.0.1:8001/admin/login/?next=/admin/"
    
    # Logging in
    browser.open_available_browser(ip)
    browser.input_text("id:id_username", "jayant")
    browser.input_text("id:id_password", "jayant")
    browser.submit_form()

    # Clicking on blog and new blog
    browser.click_link("/admin/muda_management_blog/blog/")
    browser.click_link("/admin/muda_management_blog/blog/add/")
    # Getting the title and content
    title,content = open_word_doc()

    # Filling the form
    for x in range(len(title)):
        try: 
            browser.input_text("id:id_title", title[x])
            browser.input_text("id:id_description", content[x])
            browser.select_from_list_by_value("id:id_author", "4")
            browser.select_from_list_by_value("id:id_category", "4")
            browser.select_from_list_by_value("id:id_published", "DRAFT")
            browser.select_from_list_by_value("id:id_visibility", "PUBLIC")
            browser.click_button("_save")
            browser.click_link("/admin/muda_management_blog/blog/add/")

        except Exception as e:
            print (e)
            print("Blog number:"+str(x)+" posting failed")

def automate_via_api():
    title,content = open_word_doc()
    # Ip of blog post API
    for x in range(len(title)):
        url = "http://127.0.0.1:8001/blog"
        payload = {
            "title": title[x],
            "description": content[x],
            "author_id" : 4,
            "category_id" : 4,
            "published": "DRAFT",
            "visibility": "PUBLIC"
        }
        
        try:
            data = requests.post(url,json = payload)
            if data.status_code == 200:
                print("Blog posted successfully")
            else:
                print("Blog number:"+x+" posting failed")
        except:
            print("Blog number:"+x+" posting failed")
    

def main():
    try:
        automate_via_gui()
        # automate_via_api()
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()