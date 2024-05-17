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


