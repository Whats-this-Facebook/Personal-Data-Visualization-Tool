#!/usr/bin/env python
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

def main():
    #gui.set_colors()
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
            window = gui.set_window()
            data = readFolder.Facebook(my_facebook_path)
            comments = data.comments()
            comments_string = readFolder.comments_str(comments)

        elif event == 'Open Folder':
            print('Open folder')
            window.close()
            window = gui.set_window_with_info()

        elif event == 'Privacy':
            sg.popup(privacy)

        elif event == 'Terms and Conditions':
            sg.popup(terms)

        elif event == 'vis1':
            figure = wordCounter.freqWords2Barchart(comments_string)
            vis_window, window = gui.show_vis(figure,window)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break

        elif event == 'vis2':
            figure = appsUsed.plotApps(my_facebook_path)
            vis_window, window = gui.show_vis(figure,window)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis3':
            figure = dataQuantity.plotDataQuantity("", data.folder)
            vis_window, window = gui.show_vis(figure,window)

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
            vis_window, window = gui.show_vis_list(activityList, window)
            figure_agg = None

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break

                if figure_agg:
                    # ** IMPORTANT ** Clean up previous drawing before drawing again
                    offFBActivity.delete_figure_agg(figure_agg)

                # get first listbox item chosen (returned as a list)
                choice = vis_values['-LISTBOX-'][0]

                figure = offFBActivity.plotActivities(data,choice)

                figure_agg = offFBActivity.draw_figure(
                vis_window['-CANVAS-'].TKCanvas, figure)  # draw the figure

                if vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis5':
            figure = accountActivityLocations.plotLocations(my_facebook_path)
            vis_window, window = gui.show_vis(figure,window,toolbar=True)

            while True:
                vis_event, vis_values = vis_window.read()
                if vis_event == sg.WIN_CLOSED:
                    break
                elif vis_event == 'Back':
                    window = gui.set_window()
                    vis_window.close()
                    break
        elif event == 'vis6':
            figure = usage_timeline.plot(data)
            vis_window, window = gui.show_vis(figure, window,toolbar=True)
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

