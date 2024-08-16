.. SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com/>
..
.. SPDX-License-Identifier: CC-BY-NC-SA-4.0

================
 Getting Started 
================

In this section, we are going to explore the essential steps for signing in to your Carbonio web client. Properly signing in is the first step towards accessing your emails and utilizing the various features offered by the platform. We will cover everything from accessing the webmail address to navigating through two-factor authentication (2FA) and using SAML functionality. Additionally, we will discuss how to sign out securely, recover forgotten passwords, change your login credentials, and other configurations. 

Signing In
==========

To access your Carbonio web client, the initial step is to sign in. This can be easily accomplished by navigating to your company's webmail address via your browser. To do so, you can simply follow these steps:

1.	**Open Your Browser**: Start by opening your web browser (like Chrome, Firefox, or Safari).
2.	**Enter the Webmail Address**: In the address bar at the top of your browser, type in your company’s webmail address. If you are not sure what it is, ask your company’s system administrator for help.
3.	**Sign In**: Once you have reached the webmail page, you will see a login screen. Enter your username (usually in the format of name.surname@companyname.com) and your password.
4.	**Click LOGIN**: After entering your credentials, click the LOGIN button. This will verify your identity.
5.	**Access Your Webmail**: You will now be redirected to your webmail interface. From here, you can easily read and send emails.
6.	**Watch Out for 2FA**: Sometimes, you might encounter a second-factor authentication (2FA) prompt after your initial login. If that happens, follow the additional steps below to complete the login process.

    .. image:: /img/usage/loginpage.png
        :align: center
        :width: 100%


Using Two-factor Auth (2FA)
===========================

Two-factor Authentication (2FA) is a security feature activated by your system administrator. In this case, accessing your webmail requires a secondary layer of identification for enhanced security.

When accessing your account for the first time, you will be prompted to create a **one-time password (OTP)**.

1.	First-Time Setup:

* After creating the OTP, a QR code will appear on your screen
* Install the Google Authenticator app on your mobile device

2.	Scanning the QR Code:

* Open the Google Authenticator app
* Tap the + button in the bottom right corner
* Use the app to scan the QR code displayed on your computer screen
* This creates an instance in the app that generates a temporary code that updates every 30 seconds

3.	Logging In with 2FA:

* Next time you log in to your Carbonio webmail, follow these steps:

    > Enter your **username** and **password**;
    
    > If prompted for the second-factor authentication, open the Google Authenticator app;

    > Insert the **code** from the app on your login page;

    > Click **LOGIN**.

Setting Up Two-factor Auth (2FA)
================================


If you are not forced to use 2FA on your login prompts, you can manually set it up via your web client settings. By following these steps, you will enhance the security of your Carbonio webmail account.

1.	Accessing Settings:

* Click on the **gear icon** located in the left sidebar of your webmail interface.
* Navigate to the **Auth** section. 

2.  Creating an OTP Label:

*	In the Auth section, click on **OTP Authentication**.
*	Click the **NEW OTP** + button.
*	Insert a **label** to help you remember this OTP (e.g., “mySamsungPhone”).
*	Hit the CREATE PASSWORD button.

3.	Install Google Authenticator:

*	Install the **Google Authenticator app** on your mobile device (available on both Android and iOS).
*	Open the app and press the “+” button in the bottom right corner.

4.	Scanning the QR Code:

*	Use the app to **scan the QR code** displayed during the setup process.
*	This creates an instance in the app that generates a **temporary code** that updates every 30 seconds.

5.	Logging In with 2FA:

*	The next time you log in to your Carbonio webmail, follow these steps:

        > Enter your **username** and **password**;
    
        > If prompted for the second-factor authentication, open the Google Authenticator app;

        > Insert the **code** from the app on your login page;

        > Click **LOGIN**..


Using SAML to Sign In
=====================

**SAML** stands for **Security Assertion Markup Language**. It is like a secret handshake between different websites and apps to make sure you are who you say you are. Imagine it as a special pass that lets you into multiple places without needing a separate key for each door. 

You have generally two ways to use SAML functionality to sign in to your Carbonio account:

1. First Flow:

*	When logging in to Carbonio webmail, look for the **LOGIN SAML** button.
*	Click it, and it will automatically sign you into your webmail.
*	Important: You must already be logged into your **identity provider service** (like Okta or other services provided by your system administrator).
*	If you are not sure how to log into your identity provider, reach out to your **system administrator** for assistance.

2. Second Flow:

*	First, log in to your **identity provider service** (e.g., Okta or other services provided by your system administrator).
*	Once you are logged in there, simply click on the **Carbonio mail app**.
*	SAML will seamlessly take you to your webmail without requiring you to insert your credentials.


Signing Out
===========

To ensure the security of your Carbonio web client, it is essential to sign out when you are away from your computer. Here are two straightforward methods to log out:

1. Using the Account Icon:

*	Click on the account icon located in the top-right corner of the webmail interface.
*	Select the **Logout** button.
*	You will be securely signed out.

2. Via General Settings:

*	Click the **gear icon** on the left sidebar panel to access settings.
*	Navigate to General Settings.
*	In the **Account** section, click the **LOGOUT** button, and you will be successfully logged out.

For security purposes, your system administrator might set a maximum duration for your login session.

When your session is about to expire, you will be notified in advance through the bottom left bar, which will display the remaining time: 10 minutes, 3 minutes, and 60 seconds before the session ends, respectively. In the snackbar, you will find the option to return to the login page.
You can simply log back in as usual to continue working.

In Case of Forgetting Your Password
===================================

To start the password recovery procedure, you need to enter the recovery address in the **Auth** panel, in the **Settings** section. Alternatively, you can ask the administrator to set up a recovery e-mail for your account.

.. note:: If in the Auth panel - Settings section - you do not see the field to set a recovery address, it means that the administrator has not enabled your account for the recovery process.

If you forgot your password, follow these steps:

.. image:: /img/usage/forgot-password.png
            :align: center
            :width: 100%


1.	Click on the **Forget Password?** Button, from the login page.
2.	Enter your username.
3.	You will receive an email at your recovery email address.
4.	A temporary **validation code**, that expires in twenty-four hours, will be sent to the recovery e-mail address.
5.  Copy it and insert it, then click the :bdg-primary:`VALIDATE CODE` button.
6.  If the code is validated, you can :bdg-primary-line:`CONTINUE WITH YOUR SESSION`, access your mailbox and then add a new password in the Settings's module, where you can also change the recovery address. 

If your system administrator has not configured a recovery email for your account, or you have not inserted your own recovery email address, when you attempt to insert your username to receive the password recovery email, you will encounter an error message. 

The error will prompt you to **contact your system administrator**. In this scenario, **the only way to log into your account** is by seeking assistance from your system administrator.


Changing Your Password
======================

Resetting a password becomes necessary when you want to update your existing password due to security reasons or any other relevant factors. To change your password, you must be logged into your account. Here are the steps to change your password:

1.	Log into your account.
2.	Click on the **settings** (gear icon) located in the left sidebar.
3.	Select **Auth**.
4.	Click on Change Password.
5.	Enter your **old password** along with your new password.
6.	Click the **CHANGE PASSWORD** button.

    .. image:: /img/usage/change-password.png
        :align: center
        :width: 100%


Introduction of Carbonio Web Client
===================================

When you log in to check your emails, the **Carbonio web client interface** greets you with the following components:

    .. image:: /img/usage/interface.png
        :align: center
        :width: 100%


1.	**Left Sidebar**: This section provides navigation options and quick access to various features such as Mails, Calendars, Contacts, etc.
2.	**Navigation Panel**: Here, you will find additional context related to the active feature you have selected from the left sidebar. For example, if you select “Mails” from the left sidebar, you will find access to your inboxes and email folders here.
3.	**Main Panel**: The central area displays your actual content related to the active feature you have selected from the left sidebar. For example, if you select “Mails” from the left sidebar, you will see your emails in this area; similarly, choosing “Calendars” will display your calendar events.

Using Browser Buttons to Navigate Carbonio
==========================================

It is recommended to avoid using your browser’s navigation buttons too frequently, especially when you are in the middle of composing an email or a message. These buttons can inadvertently disrupt your work and cause you to lose what you are doing. So, proceed with caution.

1.	**Back Button**: You can use your browser’s back button to return to the previous page you were viewing on Carbonio.
2.	**Forward Button**: If you have gone back and want to revisit a page you just left, click the forward button.
3.	**Avoid Reload/Refresh**: Be cautious with the reload or refresh button. Clicking it restarts your session, which can be especially dangerous when composing a new email or a lengthy text message. You might lose your work.

Account Personalization
=======================

Before you start using the Carbonio web client, take a moment to personalize your account. You can customize visual aspects such as the theme, as well as other account settings like your time zone. Most of these options are conveniently accessible in the **Settings** menu. To access it, simply click the gear icon on the left sidebar, and then select **General Settings**.


Changing Theme
==============

A theme in the Carbonio web client defines the color scheme used for its appearance. Currently, there are **two themes** available: **Dark mode** and **Light mode**. Here is how you can manage them:

1.	To **activate Dark mode**, follow these steps:

*	Go to **Settings** (gear icon) from the left sidebar.
*	Select General Settings.
*	Under **Theme Options**, open the dropdown menu.
*	Click on **Enabled**.
*	Click on the **SAVE** button located in the **top right corner** of the screen.

2.	To **disable Dark mode**, follow these steps:

*	Click on **Disabled** in the same dropdown menu and click **SAVE**.

3.	If you choose **Auto**, Carbonio will adapt to your **operating system’s default theme**. For example:

*	If your OS theme is dark, Carbonio will also be in dark mode.
*	If your OS theme is light, Carbonio will match that as well.

    .. image:: /img/usage/dark-mode.png
        :align: center
        :width: 100%


Changing Font Size
==================

You can change the font size across all Carbonio web clients according to your preferences. To change the font size simply follow these steps:

1.	Open the **Settings** (gear icon) from the left sidebar.
2.	Select General Settings.
3.	Under the **Appearance** section, find the slider for adjusting the font size.
4.	If you want to manually control the font size, uncheck the option that says *Automatically resize the text size depending on the device*.
5.	Use the slider to set the font size to your preference. As you move the slider, you will see the results in the bottom box with some dummy text.
6.	Once you are satisfied, click **SAVE** in the top right corner.

Remember, if you prefer automatic resizing based on the device, you can leave the checkbox checked. Otherwise, adjust the font size manually using the slider.

    .. image:: /img/usage/font-size.png
            :align: center
            :width: 100%


Changing Your Time Zone
=======================

As a digital workspace, Carbonio relies on precise time zone settings to ensure optimal performance for calendars and other features like emails, guaranteeing accurate timestamps. This becomes particularly crucial when collaborating with colleagues across different countries and time zones. To change your time zone, follow these steps:

1.	Open the **Settings** (gear icon) from the left sidebar.
2.	Select General Settings.
3.	Under the **Time Zone and Language** section select the dropdown menu for **Time Zone** and choose your time zone.
4.	Click **SAVE** in the top right corner.

    .. image:: /img/usage/time-zone.png
            :align: center
            :width: 100%


Changing Carbonio Language
==========================

To change your Carbonio web client language, follow these steps:

1.	Open the **Settings** (gear icon) from the left sidebar.
2.	Select General Settings.
3.	Under the **Time Zone and Language** section select the dropdown menu for **Language** and choose your language.
4.	Click **SAVE** in the top right corner.

Accessing Multiple Accounts
===========================

On the Carbonio web client, you have access to multiple accounts. Let's say you have your personal account, as well as two additional accounts created for HR tasks and communications with your colleagues under the name “hr@example.com”, and another one named “info@example.com” for external communications of the company. **Only your system administrator can add these accounts and grant you access** to manage them via your main account.

    .. image:: /img/usage/inbox-multiple-accounts.png
            :align: center
            :width: 100%

So, when you sign into your main account, you will see these two additional accounts listed under your main account. To access these accounts, simply click on the downward arrow next to their names to open a dropdown menu. From there, you can access the inbox and other folders within each account.