# AI uBlock Origin Blacklist
A personal list for [uBlock Origin](https://github.com/gorhill/uBlock) blocking AI content farms. Pull requests welcome.

## Install
You can [click here](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw%2Egithubusercontent%2Ecom%2Falvi%2Dse%2Fai%2Dublock%2Dblacklist%2Fmaster%2Flist%2Etxt&title=AI%20Content%20Farms) to subscribe to this list automatically. This link works only if you have uBlock Origin installed.

Alternatively, import the following URL as a 3rd party list in uBlock Origin.
* `https://raw.githubusercontent.com/alvi-se/ai-ublock-blacklist/master/list.txt`

## Why?
While browsing it happens ~sometimes~ [**most of the times**](https://www.axios.com/2025/10/14/ai-generated-writing-humans) that I come across websites which text is written by generative AI. These websites provide no useful information, have mediocre content and are filled up with ads and referral links to earn money.
So when I find this kind of website, I put it here.

The key idea is simple: if I wanted my question to be answered by AI, *I* would ask AI. If I'm searching online, it means that I want an answer written by a person. A person has experience, opinions, ideas, creativity and a lot more information that might want to share with the web. AI doesn't.

What's more, AI content can also be **dangerous**: articles in content farms are not checked by anyone before being published, since they are massively generated. An AI might hallucinate when writing about dangerous topics: it might suggest you to short-circuit on your circuit board. Or to execute dangerous commands on your PC such as `rm -rf /`. Or to mix bleach and ammonia (DON'T DO THESE THINGS). AI generated content is not reliable, and if no one is checking what is being published, it needs to be blocked.

As I said, I'm adding pages as I browse, so each entry is added manually. I'm not considering using automated tools simply because it's hard for an algorithm to understand if a page is AI generated or not, especially with the guidelines I wrote next. An argument could be that this list is useless because it's too short. However, since these websites are doing SEO to appear first on search engines, you will meet the same website more than once, especially for searches related to each other. I've found this list to be blocking websites since the very first day I began writing it, even with very few entries.

However, there is indeed some bias for my entries. For example, as I am an Italian citizen, you will find a lot of Italian websites. This is another reason why pull requests are welcome.

## How to add websites
If you're not a technical user and don't know how GitHub works, simply report your suspects creating an issue, by clicking [here](https://github.com/alvi-se/ai-ublock-blacklist/issues/new).


If you want to create a pull request, here's how to add a website to the list.
First, try to find the scope of the AI spammer. Usually, it will be a domain, but I've found also a lot of Medium blogs or dev.to blogs. These platforms should not be blocked as a whole, but just the blog who's spamming.

Say that you want to add entry `example.com/@slopUser`, simply put a line to file `list.txt` as following:
```adblock
||example.com/@slopUser^$doc
```

The whole `example.com` domain hosts AI garbage, you say? Add only the domain:
```adblock
||example.com^$doc
```

If you really hate AI and have a lot of time to spend, you are welcome to do some research about the website you have found. Most of these content farms are built by people or organizations [who sell SEO and digital marketing](https://www.fiverr.com/categories/online-marketing/seo-services/seo-packages).
If you find the source, you might also find other content farms they have created. If you do, add them at the bottom of the file.


## How websites are added
Content farm have have some patterns that make them recognizable. Here are the ones I understood. Of course, these are not strict rules.

* **Unnecessary introduction and conclusion**: this is probably the easiest way to spot content farms. Often, the intro is also annoyingly baroque. For example, you click on some guide on how to use a specific feature in Flutter.
  The article would begin giving an introduction about Flutter itself like the following:
  > In today’s fast-moving digital landscape, users expect apps to be fast, beautiful, and consistent across every device they touch.
  
  Probably, no human would write such an introduction to explain a *specific* feature.
  It could fit to generally speak about Flutter (still too baroque though), but not for a super specific code that can be understood only by experienced developers. If I'm writing such an article, I'm supposing that the reader will already know what Flutter is!
* **\[topic\]: A Comprehensive Guide/A Step-To-Step Guide/Ultimate Guide**: LLMs love these catchphrases for titles of tutorials and guides.
* **No/few links to external content**
* **No sources and references**: same as above, but for sources about facts. This is very important to check, especially for articles about (pseudo)science, politics and content that could spread misinformation.
* **Referral links everywhere**: content farms are there just to make money. I've personally seen sites shamelessly putting purchase advice in navbars or footers.
* **Reference to product of company**: the website is owned by a company that sells some product or service. The page will probably be like "How to solve \[problem\]" -> buy our product.
* **Blog with hundreds of thousands of articles**: especially when published in a very short time span. A lot of AI slop blogs post tens or hundreds of articles a day, mostly by the same author.
* **Hallucinations**: the content is plain wrong.
* **Date after November 2022**: the AI hype began with the release of ChatGPT in November 2022. A weak guideline for sure, but it adds up to all others. Dates can be easily faked though.
* **No/few images, videos, non-text media**: these pages are automatically generated and published, and it's hard to generate other kind of content to be put into the page.
* **AI generated images, logos**: usually it's the banner of the article or the blog logo.
* **Poor text formatting**
* **Not-rendered Markdown characters**: text has no formatting and has Markdown syntax.
* **Long post, with unnecessary or out-of-context content**: at some point the article can start talking about another topic, which can be related to the original one but irrelevant.
* **Always on top of search engines result**: they are of course abusing SEO.
* **Know-it-all blog**: the same blog appears in the search engine for completely different topics.
* **Vague content**: lots of headings, each with a short content that provides no useful information.
* **Unprofessional or missing contact information**: they have bought a domain, why are they using Gmail for contact?
* **Vague or missing about page**
* **AI enthusiastic content**: if someone loves ChatGPT they will use it for **everything**. So if you stumble across an AI-devoted blog, it's for sure 100% AI generated.


## Google Dorks
Because AI users are dumb enough to copy-paste LLM responses without reading them, the LLM will sometimes reveal itself, for example in the intro of the content.
The following are some Google Dorks to find 100% AI generated pages. Such pages will have their whole domain put into the uBlock list.
Dorks can be easily generated by asking an LLM to generate naive content, for example by prompting `Generate an article for my blog about dogs`.
The LLM will answer with an intro like `Sure! Here's an article about`. Take this phrase and search it surrounded by quotes.
```
# English
"Sure! Here's an article about"

# Italian
"Certo! Ecco un articolo"
```

## NAQ (Never Asked Questions)

**My website is on your list!**

Cry about it.

**But I'm just using AI to correct grammar and spell**

All I hear is skill issue. Imagine needing an AI to write stuff.

**I bought a domain that previously was a content farm, can you remove it?**

No.

## Similar projects
- [uBlockOrigin & uBlacklist Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist): this projects hides every AI related result from search engines, including
  websites that I believe are legit tools (e.g. ChatGPT). What I want instead is blocking access only to garbage AI content farms.
