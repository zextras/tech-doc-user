.. SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com/>
..
.. SPDX-License-Identifier: CC-BY-NC-SA-4.0

=====================
 Working with Search
=====================

Searching in the Carbonio web client allows you to find emails, contacts, appointments, and files using specific criteria such as words, dates, time, URL, size, tags, read status, and file attachments. There are two types of searches available:

•	Quick Search: This is performed using the search box located on the top bar. You can search through various items, including emails, contacts, appointments, and files, based on the active feature selected from the left sidebar.
•	Advanced Search: This is performed using the search feature you can select from the left sidebar. This enables more complex searches using different filters such as date, time, subject, etc.

These search capabilities provide efficient ways to locate and manage your data within the Carbonio web client.


Using Quick Search for Different Items
======================================

You can perform a quick search using the search box located on the top bar. You can search through various items, including emails, contacts, appointments, and files, based on the active feature selected from the left sidebar.

  .. image:: /img/usage/search-bar.png
                :align: center
                :width: 100%

To do so:

#.	Select either Mails, Calendars, Contacts, or Files from the left sidebar, depending on which item you want to search for. The text of the search box changes based on which feature is active. For example, in Mails, the term is Search in Mails.
#.	Enter a keyword in the search box, such as a term used in an email subject or body that you are searching for.
#.	Click the button next to the search box with the magnifying glass icon.
#.	Your search results will appear on the left side of a list.

Using Advanced Search to Filter Your Search
===========================================

This is performed using the search feature you can select from the left sidebar.

  .. image:: /img/usage/search.png
                :align: center
                :width: 100%

To do so:

#.	Select the **Search feature** from your left sidebar.
#.	Select the search category (i.e., Mails, Calendars, Contacts, Files) from the drop-down menu next to the **NEW** button.
#.	Click on **ADVANCED FILTERS** on the left side. A new window appears.
#.	Select different filters to refine your search results.
#.	Click the **SEARCH** button.

Filters for refining search results vary depending on the category you select in step 2. For instance, in the Mails category, the filters include:	

•	**Attachment**: Search in emails that have an attachment.
•	**Flagged**: Search in flagged emails.
•	**Unread**: Search in unread email items.
•	**Include shared folders**: Include shared items in the search.
•	**Keyword**: Search for specific terms used in the email body.
•	**Subject**: Search in email subjects.
•	**From**: Search for emails received from a specific email address.
•	**To**: Search for emails sent to a specific email address.
•	**Attachment type**: Search for specific attachment formats such as PDF, text document, images, etc.
•	**Status of e-mail item**: Search for emails with specific status such as read, unread, flagged, etc.
•	**Size smaller than (MB)**: Search for emails with a size smaller than a specified number in MB.
•	**Size larger than (MB)**: Search for emails with a size larger than a specified number in MB.
•	**Sent before**: Search for emails sent before the specified date.
•	**Sent after**: Search for emails sent after the specified date.
•	**Sent on**: Search for emails sent exactly on the specified date.
•	**Tag**: Search for emails or contacts that have a specific tag.
•	**Is contained in**: Limit the search to selected folders.

Advanced Search Syntax
======================

**Syntax**: You can search for various items such as words, names, phone numbers, or domain names. However, when conducting content searches, it is essential to follow certain rules.

**Exact Text Match**: When searching for phrases, each word within the phrase must be an exact match. No spelling variants are allowed. For instance, a search for "apple" will not match with "apples".

**Case Sensitivity**: Searches are not case-sensitive. "Cat", "cat", and "CAT" are all treated as the same.

**Special Characters**: Certain special characters cannot be used in search text.

**Wildcards**: The asterisk (*) can be used as a wildcard after a prefix to broaden search results. For example, searching for "choc" retrieves items with words like "chocolate", "chocoholic", etc.

**Attachments**: System-readable file attachments are also included in searches. These are files that can be converted to HTML, such as PDF documents and text files.

**Contacts in Address Books**: When searching for contacts, the entire word or number string must be entered. For instance, to search contacts by email address, the full address as it appears in the contact entry must be used. It is not possible to search solely by domain.

**Search Language Structure**: Conducting content searches slightly differs from text-match searches or typical word-processing features such as Find.

**Keywords**: If you know where to search for your item, you can enter keywords followed by a colon and the search item in the search text box. For example, "in:inbox".

**Options:**

•	**Content**: Specifies text that must be present in the message. Example: content:important.
•	**From**: Specifies a sender's name or email address. Example: from:"john.doe".
•	**To**: Similar to "From:", but for recipients in the To: header. Example: to:"jane.smith".
•	**CC**: Similar to "From:", but for recipients in the Cc: header. Example: cc:"Manager".
•	**Subject**: Specifies text that must appear in the subject header. Example: subject:meeting.
•	**In**: Specifies a folder. Example: in:sent.
•	**Has**: Specifies an attribute that the message must have. Example: has:attachment.
•	**Filename**: Specifies an attachment file name. Example: filename:report.pdf.
•	**Type**: Specifies a search within attachments of a specified type. Example: type:excel.
•	**Attachment**: Specifies any item with a certain type of attachment. Example: attachment:word.
•	**Is**: Searches for messages with a specific status. Example: is:unread.
•	**Date**: Specifies a date. Example: date:02/20/2024.
•	**After**: Specifies mail sent after a certain date. Example: after:01/01/2024.
•	**Before**: Specifies mail sent before a certain date. Example: before:03/01/2024.
•	**Size**: Specifies emails based on their total size, including attachments. Example: size: 1MB.
•	**Smaller**: Specifies emails based on their total size, including attachments. Example: smaller:1MB.
•	**Larger**: Specifies emails based on their total size, including attachments. Example: smaller:1MB.
•	**Tag**: Finds messages tagged with a specified tag. Example: tag:important.

**Wildcards**: The asterisk (*) after a prefix serves as a wildcard to find content with words having similar spellings. For instance, "dog" retrieves items with words like "doggy", "doghouse", etc. Note: Double-byte asterisk signs in search queries are ignored during the search.









