title: "Free custom email domain through Gmail"
date: 2025-05-16
label: log
tags: [email, tutorial]
snippet: "1 CRAZY trick that Big Custom Mailbox doesn't want you to know"

Ok, so you have a CRAZY idea for a startup that you can't believe nobody's done yet, you incorporated a Delaware LLC via Stripe Atlas and bought a domain, then (vibe)coded  a dope 1-page website so the money tree investors and customers can come and find you. Ahh, life is good. Oh wait, but you can't put your <name i thought was dope in middle school>@gmail.com address in the contact, or else people will know you're just a kid. And all the alternatives cost something every month, which really cuts into your ARR. What now?? 

So if you can receive email at a custom domain (e.g. Namecheap offers free custom domain email forwarding) but can't send it, you can solve this. Gmail offers this service for free but has utterly gimped the setup guides, probably just to sell more Google Workspace. I'm gonna tell you how to do it because it's actually really simple. 

## 1. First navigate to Gmail, then hit settings, then hit all settings, then go to "Accounts and Imports"

Menu should look like this. Hit "Add another email address" to trigger a popup

{{ add_pic("freebusinessemail/0.png", "") }}

## 2. Put in your custom email

{{ add_pic("freebusinessemail/1.png", "") }}

## 3. Fill out SMTP

Use "smtp.gmail.com" and port 587, then add your current gmail address as the username (remove the @gmail.com). For password you'll need to make an app password. 

{{ add_pic("freebusinessemail/2.png", "") }}

An app password is basically a way to give an app access to your email without exposing your password. To make one, go to [myaccount.google.com](https://myaccount.google.com/), search for "App passwords" (you will not find it as a menu item), do a sign-in again, then make up a name and generate one.

{{ add_pic("freebusinessemail/3.png", "") }}

Copy that into the SMTP popup and hit Add Account:

{{ add_pic("freebusinessemail/4.png", "") }}

You are pretty much done. They will send a confirmation email to your custom domain, which, if your forwarding was really set up right, will go somewhere you can click it. From then on you can send emails from your custom domain fo free. Enjoy!

{{ add_pic("freebusinessemail/5.png", "") }}

<hr>

Guide mostly cribbed from the super-thorough but deleted Google Support guide backed up on wayback [here](https://web.archive.org/web/20230326042630/https://support.google.com/domains/answer/9437157). Why do they insist on making their products annoying to use? 
