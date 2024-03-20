.. SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com/>
..
.. SPDX-License-Identifier: CC-BY-NC-SA-4.0

Carbonio Chats is a component that provides corporate instant messaging features like text chats, 1-to-1 video calls, and videoconferencing.

The UI of Carbonio Chats is organised in three columns:

* The left-hand side column holds the list of contacts with the history of the passed chats. 
  Above it, you can |create| new chats and Groups, filter existing chat names and on the top, select between Chats and Virtual Rooms (see further on for more). 
  Below it, buttons allow to manage virtual rooms.

* The central column holds the chat messages. Above the chat’s top-right corner, click the phone icon to start a video call with the contact.

* The right-hand side column holds information about the contact and allows to copy the link to the contact’s virtual room (which is unique), mute notifications, and clear the chat’s history.

.. _chats-moderators:

Moderators in Rooms
-------------------------

The user that creates a **room** (we call *virtual room* a Group or a Virtual Room, see below) becomes automatically the **Room Moderator** and can manage the room’s textual and video conversations. In particular, the *Mute For All* and *Add new members* functionalities are reserved for Moderators only.

A moderator can promote any user as moderator and can leave the virtual room only if either no other users are present in the room or another moderator is present in the room.

Groups
-------------------------

Groups are non-persistent entities used to communicate with multiple people at the same time (by default up to 5 in total). Any user can create a group inviting people, and any group member can invite more people in the same way. When all users leave a group, the group itself ceases to exist.

Virtual Rooms
-------------------------

Virtual Rooms allow to set up video calls with multiple participants, including **Internal Guests** and **External Guests**. The former are users with an account on the current Carbonio instance, while the latter are users that have no local account (i.e., on the Carbonio instance). Both can join on a temporary basis without the need of being members of the Virtual Room.

Moreover, in the Virtual Room tab, users can see at a glance all ongoing and planned meetings involving them.

To create a new meeting, click the :bdg-primary-line:`CREATE ROOM` button, then enter a name. You will be automatically assigned the role of **Owner**. Besides being a :ref:`chats-moderators`, an owner can not be removed and is the solely person that can delete a Virtual Room.

In the left-hand side column, all meetings are shown, divided into **Ongoing Meetings** and **Scheduled meetings**. For each of them, a few buttons are shown, to join or delete a virtual room, to copy and share the virtual room’s link and to change the link.

.. note:: When a link is changed, the old one is wiped and can not be used anymore.

Planned Meetings prove useful when scheduling meetings with colleagues: create a planned meeting, then attach the virtual room’s link to the calendar’s invitation.

Video calls can be recorded, but require an additional package. Please refer to section Recording a Video Meeting for directions and more information on the functionality.

When joining a Virtual Room, a dialog window appears, which carries the name of the room and allows to choose and test the audio and video devices.

Sharing documents
-------------------------

Within a textual chat, it is possible to share files by either uploading a file from the local workstation or mobile device or by providing the public link to a file stored in Carbonio Files. To carry out the latter action, click on the paper clip icon on the right-hand side of the chat’s input box.

Moreover, most files can be previewed before being downloaded, see Section Preview for more information.

Presence
-------------------------

Presence is managed automatically in Carbonio Chats: whenever a user logs in, regardless of whether Chats has the focus, they appear as **online**.

As part of the user presence system, all messages are displayed with a variable number of check symbols:

.. card:: 

  .. image:: /img/chats/chats-message-read.png

  * 0 grey checks: message not yet delivered to the server

  * 1 grey check: message delivered to the server

  * 2 grey checks: message delivered to the recipient user  to all users in case of chats with multiple members or Virtual Rooms

  * 2 blue checks: message viewed by the recipient user  to all users in case of chats with multiple members or Virtual Rooms


When sending a text message, if privacy is enabled, then only one gray check is shown, meaning that the server has received the message. No acknowledgement will be sent back by the receiving user.

Unread Messages
-------------------------

The number of unread messages in any conversation (Group and instant meeting) appears on the right side of both the *Chats* and *Instant Meetings* label from where the message originated, and in the list of conversions underneath, next to the actual chat generating the message.