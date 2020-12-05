#!/usr/bin/env python
import os
import GUI.gui as gui
import Plots.wordCounter as wordCounter
import Plots.dataQuantity as dataQuantity
import Plots.appsUsed as appsUsed
import CLI.comments as comments
import CLI.readFolder as readFolder
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import Plots.offFBActivity as offFBActivity
import Plots.accountActivityLocations as accountActivityLocations
import Plots.usage_timeline as usage_timeline

my_facebook_path = ""
figure_dict = {}

def frontloader(data, my_facebook_path):
    print("Entering frontloader")
    comments = data.comments()
    messages = data.messages()
    posts    = data.posts()
    name     = data.profile()['name']['full_name']
    comments_string = readFolder.comments_str(comments)
    messages_string = readFolder.messages_str(messages, name)
    posts_string    = readFolder.posts_str(posts)
    print(messages_string)
    print("generating visualization 1")
    figure_dict["vis1"] = wordCounter.freqWords2Barchart(comments_string + messages_string + posts_string)
    print("generating visualization 2")
    figure_dict["vis2"] = appsUsed.plotApps(my_facebook_path)

    print("generating visualization 3")
    figure_dict["vis3"] = dataQuantity.plotDataQuantity("", data.folder)

    print("generating visualization 4")
    figure_dict["vis4"] = offFBActivity.get_offFBActivity_Data_Dictionary(data)

    print("generating visualization 5")
    figure_dict["vis5"] = accountActivityLocations.plotLocations(my_facebook_path)

    print("generating visualization 6")
    figure_dict["vis6"] = usage_timeline.plot(data)

    print("generating complete")



def description_dict(my_facebook_path):
    d = {}
    d["vis1"] = ("The above figure shows the frequency of each of your most written words on Facebook.\n" 
        + "The data used for this visualization can be found in:\n"
        + os.path.join(os.path.join(my_facebook_path, "comments"),"comments.json") + "\n"
        + os.path.join(os.path.join(my_facebook_path, "posts"),"your_posts_1.json") + "\n"
        + os.path.join(os.path.join(my_facebook_path, "messages"),"inbox"))

    d["vis2"] = ("The above figure shows a timeline of every app and website you have used that Facebook knows about.\n"
        + "Use the toolbar's maginfiying glass on the top left to zoom in to areas on the timeline that have overlapping apps.\n"
        + "The data used for this visualization can be found in:\n"
        + os.path.join(os.path.join(my_facebook_path, "apps_and_websites"),"apps_and_websites.json"))

    d["vis3"] = "The above figure shows the quantity of data per category in your Facebook folder" 
    
    d["vis4"] = ("The above figure shows your off-Facebook activity that Facebook knows about.\n"
        + "The data used for this visualization can be found in:\n"
        + os.path.join(os.path.join(my_facebook_path, "ads_and_businesses"),"your_off-facebook_activity.json"))

    d["vis5"] = ("The above figure shows a map of every location Facebook has tracked you\n"
        + "The data used for this visualization can be found in:\n"
        + os.path.join(os.path.join(my_facebook_path, "security_and_login_information"),"account_activity.json"))

    d["vis6"] = ("The above figure shows a timeline of your sent messages, posts, and comments over time.\n"
        + "The data used for this visualization can be found in:\n"
        + os.path.join(os.path.join(my_facebook_path, "messages"),"inbox") + "\n"
        + os.path.join(os.path.join(my_facebook_path, "profile_information"),"profile_information.json") + "\n"
        + os.path.join(os.path.join(my_facebook_path, "comments"),"comments.json") + "\n"
        + os.path.join(os.path.join(my_facebook_path, "posts"),"your_posts_1.json"))
    return d

def main():
    gui.set_colors()
    window = gui.set_window_with_info()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'info':
            sg.popup(f'''About This App\n\nVisualize your Facebook data!\n\n\n''')

        elif event == 'Go':
            my_facebook_path = values['Browse']
            window.close()
            data = readFolder.Facebook(my_facebook_path)
            frontloader(data, my_facebook_path)
            desc_dict = description_dict(my_facebook_path)
            window = gui.set_window()

        elif event == 'Open Folder':
            print('Open folder')
            window.close()
            window = gui.set_window_with_info()

        elif event == 'Privacy':
            sg.popup(privacy)

        elif event == 'Terms and Conditions':
            sg.popup(terms)

        elif event == 'vis1':
            figure = figure_dict["vis1"]
            desc = desc_dict["vis1"]
            vis_window, window = gui.show_vis(figure,window,desc)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break

        elif event == 'vis2':
            figure = figure_dict["vis2"]
            desc = desc_dict["vis2"]
            vis_window, window = gui.show_vis(figure,window,desc,toolbar=True)
            

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis3':
            figure = figure_dict["vis3"]
            desc = desc_dict["vis3"]
            vis_window, window = gui.show_vis(figure,window,desc)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis4':
            activityList = data.offFB_activities_list()
            desc = desc_dict["vis4"]
            vis_window, window = gui.show_vis_list(activityList, window, desc)

            figure = offFBActivity.placeHolderMsg()
            figure_agg = offFBActivity.draw_figure(
                    vis_window['-CANVAS-'].TKCanvas, figure)  # draw the figure

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break

                if figure_agg:
                    # ** IMPORTANT ** Clean up previous drawing before drawing again
                    offFBActivity.delete_figure_agg(figure_agg)

                if len(vis_values['-LISTBOX-']) > 0:
                    # get first listbox item chosen (returned as a list)
                    choice = vis_values['-LISTBOX-'][0]

                    figure_data = figure_dict["vis4"][choice]
                    figure = offFBActivity.get_figure(figure_data)

                    figure_agg = offFBActivity.draw_figure(
                    vis_window['-CANVAS-'].TKCanvas, figure)  # draw the figure

                if vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis5':
            figure = figure_dict["vis5"]
            desc = desc_dict["vis5"]
            vis_window, window = gui.show_vis(figure,window,desc,toolbar=True)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis6':
            figure = figure_dict["vis6"]
            desc = desc_dict["vis6"]
            vis_window, window = gui.show_vis(figure, window,desc,toolbar=False)
            figure_agg = None

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break



privacy = '''Privacy Policy
Group 5 built the Facebook Visualization Tool app as an Open Source app. This SERVICE is provided by Group 5 at no cost and is intended for use as is.
This page is used to inform visitors regarding my policies with the collection, use, and disclosure of Personal Information if anyone decided to use my Service.
If you choose to use my Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that I collect is used for providing and improving the Service. I will not use or share your information with anyone except as described in this Privacy Policy.
The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which is accessible at Facebook Visualization Tool unless otherwise defined in this Privacy Policy.

Information Collection and Use
For a better experience, while using our Service, I may require you to provide us with certain personally identifiable information. The information that I request will be retained on your device and is not collected by me in any way.
Link to privacy policy of third party service providers used by the app
Facebook

Service Providers
I may employ third-party companies and individuals due to the following reasons:
To facilitate our Service;
To provide the Service on our behalf;
To perform Service-related services; or
To assist us in analyzing how our Service is used.
I want to inform users of this Service that these third parties have access to your Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.

Changes to This Privacy Policy
I may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. I will notify you of any changes by posting the new Privacy Policy on this page.
This policy is effective as of 2020-11-04

Contact Us
If you have any questions or suggestions about my Privacy Policy, do not hesitate to contact me at [mail].
This privacy policy page was created at privacypolicytemplate.net and modified/generated by App Privacy Policy Generator'''

terms = '''Terms & Conditions

By downloading or using the app, these terms will automatically apply to you – you should make sure therefore that you read them carefully before using the app. You’re not allowed to copy, or modify the app, any part of the app, or our trademarks in any way. You’re not allowed to attempt to extract the source code of the app, and you also shouldn’t try to translate the app into other languages, or make derivative versions. The app itself, and all the trade marks, copyright, database rights and other intellectual property rights related to it, still belong to Group 5.
Group 5 is committed to ensuring that the app is as useful and efficient as possible. For that reason, we reserve the right to make changes to the app or to charge for its services, at any time and for any reason. We will never charge you for the app or its services without making it very clear to you exactly what you’re paying for.
The Facebook Visualization Tool app processes personal data that you have provided to us, in order to provide my Service. It’s your responsibility to keep your access to the app secure.
The app does use third party services that declare their own Terms and Conditions.

With respect to Group 5’s responsibility for your use of the app, when you’re using the app, it’s important to bear in mind that although we endeavour to ensure that it is updated and correct at all times, we do rely on third parties to provide information to us so that we can make it available to you. Group 5 accepts no liability for any loss, direct or indirect, you experience as a result of relying wholly on this functionality of the app.
At some point, we may wish to update the app.We may also wish to stop providing the app, and may terminate use of it at any time without giving notice of termination to you. Unless we tell you otherwise, upon any termination, (a) the rights and licenses granted to you in these terms will end; (b) you must stop using the app, and (if needed) delete it from your device.
Changes to This Terms and Conditions
I may update our Terms and Conditions from time to time. Thus, you are advised to review this page periodically for any changes. I will notify you of any changes by posting the new Terms and Conditions on this page.
These terms and conditions are effective as of 2020-11-04

Contact Us
If you have any questions or suggestions about my Terms and Conditions, do not hesitate to contact me at [mail].
This Terms and Conditions page was generated by App Privacy Policy Generator
'''

if __name__ == "__main__":
    main()

