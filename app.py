<!DOCTYPE html><html lang="en" class="optimisticai_d4925249-module__WZtcjq__variable optimisticmono_9b82a078-module__hMSRWa__variable light"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><link rel="stylesheet" href="/_next/static/immutable/chunks/0_n83orcwyk4s.css" data-precedence="next"/><link rel="stylesheet" href="/_next/static/immutable/chunks/0pgin19elqu3q.css" data-precedence="next"/><link rel="stylesheet" href="/_next/static/immutable/chunks/42e7h9g2vn8e3.css" data-precedence="next"/><link rel="stylesheet" href="/_next/static/immutable/chunks/287l5xq35imjj.css" data-precedence="next"/><link rel="stylesheet" href="/_next/static/immutable/chunks/17oghy4n4g9qf.css" data-precedence="next"/><link rel="preload" as="script" fetchPriority="low" href="/_next/static/immutable/chunks/36baba7il59p9.js"/><script src="/_next/static/immutable/chunks/1xfwe67b8hkhb.js" async=""></script><script src="/_next/static/immutable/chunks/2nqiqj-lrk2yk.js" async=""></script><script src="/_next/static/immutable/chunks/turbopack-3dyxe4o3y_28h.js" async=""></script><script src="/_next/static/immutable/chunks/1dq47j4p-xg3o.js" async=""></script><script src="/_next/static/immutable/chunks/0plfqy-1kt7-q.js" async=""></script><meta name="next-size-adjust" content=""/><script>(function(){try{var d=document.documentElement,m=window.matchMedia("(prefers-color-scheme: dark)");function a(){var c=d.classList;if(m.matches){c.remove("light");c.add("dark");}else{c.remove("dark");c.add("light");}}a();m.addEventListener("change",a);}catch(e){}})()</script><meta name="sentry-trace" content="429c48ce1d7e4325a24bc947a98cf882-83a219f7ee388179-0"/><meta name="baggage" content="sentry-environment=production,sentry-release=46df86a47c8d6e39844e1979f4c66c115d1e82c2,sentry-public_key=217336c598020d63d1a44137ff8fdb71,sentry-trace_id=429c48ce1d7e4325a24bc947a98cf882,sentry-org_id=4509963614355457,sentry-sampled=false,sentry-sample_rand=0.9101045391771607,sentry-sample_rate=0.1"/><script src="/_next/static/immutable/chunks/0cz1d0mv5g_q7.js" noModule=""></script></head><body><div hidden=""><!--$--><!--/$--></div><div class="min-h-dvh px-6 pt-8 pb-8 font-mono text-[14px] leading-[1.6]"><pre class="mx-auto flex max-w-[1000px] items-start bg-transparent"><div class="text-text-tertiary border-fill-divider me-4 min-w-[40px] shrink-0 border-e pe-4 text-end select-none" aria-hidden="true"><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div><div>8</div><div>9</div><div>10</div><div>11</div><div>12</div><div>13</div><div>14</div><div>15</div><div>16</div><div>17</div><div>18</div><div>19</div><div>20</div><div>21</div><div>22</div><div>23</div><div>24</div><div>25</div><div>26</div><div>27</div><div>28</div><div>29</div><div>30</div><div>31</div><div>32</div><div>33</div><div>34</div><div>35</div><div>36</div><div>37</div><div>38</div><div>39</div><div>40</div><div>41</div><div>42</div><div>43</div><div>44</div><div>45</div><div>46</div><div>47</div><div>48</div><div>49</div><div>50</div><div>51</div><div>52</div><div>53</div><div>54</div><div>55</div><div>56</div><div>57</div><div>58</div><div>59</div><div>60</div><div>61</div><div>62</div><div>63</div><div>64</div><div>65</div><div>66</div><div>67</div><div>68</div><div>69</div><div>70</div><div>71</div><div>72</div><div>73</div><div>74</div><div>75</div><div>76</div><div>77</div><div>78</div><div>79</div><div>80</div><div>81</div><div>82</div><div>83</div><div>84</div><div>85</div><div>86</div><div>87</div><div>88</div><div>89</div><div>90</div><div>91</div><div>92</div><div>93</div><div>94</div><div>95</div><div>96</div><div>97</div><div>98</div><div>99</div><div>100</div><div>101</div><div>102</div><div>103</div><div>104</div><div>105</div><div>106</div><div>107</div><div>108</div><div>109</div></div><code class="block min-w-0 flex-1 overflow-x-auto whitespace-pre"><pre class="shiki shiki-themes github-light github-dark" style="--shiki-light:#24292e;--shiki-dark:#e1e4e8;--shiki-light-bg:#fff;--shiki-dark-bg:#24292e" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">import</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">import</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> requests</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">from</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> flask </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">import</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> Flask, request</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">app </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> Flask(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">__name__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">SHEET_ID</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"SHEET_ID"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"1cCXED4MnPNNqAKdsXFPyhqbM60_AJqE3cQHSkBAj7Ls"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">WHATSAPP_TOKEN</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"WHATSAPP_TOKEN"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">""</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">PHONE_NUMBER_ID</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"PHONE_NUMBER_ID"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">""</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">VERIFY_TOKEN</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"VERIFY_TOKEN"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"ammar_clinic_2026"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">GROQ_API_KEY</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> =</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> os.getenv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"GROQ_API_KEY"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">""</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0"> get_sheet_csv</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">(sheet_name):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">    try</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">:</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        url </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"https://docs.google.com/spreadsheets/d/</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">{SHEET_ID}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">/gviz/tq?tqx=out:csv&#x26;sheet=</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">{</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">sheet_name</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        r </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> requests.get(url, </span><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70">timeout</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">10</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">        if</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> r.status_code </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">==</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF"> 200</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">            return</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> r.text[:</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">3000</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">]  </span><span style="--shiki-light:#6A737D;--shiki-dark:#6A737D"># first 3000 chars</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">        return</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF"> ""</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">    except</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">        return</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF"> ""</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0"> build_prompt</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">():</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">    services </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> get_sheet_csv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Services_الخدمات"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">    settings </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> get_sheet_csv(</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Settings_الاعدادات"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">)</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">    return</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"""</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">أنت موظف استقبال عيادة الدكتور عمار حسين الراوي - عيادة أمل الراوي.</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">تتكلم عراقي مهذب و مختصر.</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">الخدمات والأسعار من الشيت:</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">{</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">services</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">}</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">الإعدادات:</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">{</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">settings</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">}</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">قواعد:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">1. ابدأ بـ: أهلاً وسهلاً بيك في عيادة أمل الراوي 🌿</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">2. إذا سأل عن سعر خذه من الشيت</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">3. لا تشخص طبياً أبداً</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">4. للحجز اطلب الاسم والوقت</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">5. انهي بـ: دوامنا 3:30-10 مساءً - الجمعة عطلة - 0780540459</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"""</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0"> ask_ai</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">(user_msg):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">    if</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> not</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF"> GROQ_API_KEY</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">:</span></span>
<span class="line"><span style="--shiki-light:#6A737D;--shiki-dark:#6A737D">        # fallback without AI - use sheet data directly</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">        return</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583"> f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"أهلاً وسهلاً بيك في عيادة أمل الراوي 🌿</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">\n\n</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">سؤالك: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">{</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">user_msg</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">}\n\n</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">تكدر تتواصل ويانا مباشرة: 0780540459</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">\n</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">دوامنا من 3:30 عصراً للـ 10 مساءً - الجمعة عطلة"</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">    </span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">    prompt </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> build_prompt()</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">    try</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">:</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        url </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF"> "https://api.groq.com/openai/v1/chat/completions"</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        headers </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> {</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Authorization"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Bearer </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">{GROQ_API_KEY}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"Content-Type"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"application/json"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        data </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> {</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">            "model"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"llama-3.1-8b-instant"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">,</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">            "messages"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: [</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">                {</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"role"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"system"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"content"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: prompt},</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">                {</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"role"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"user"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">"content"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: user_msg}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">            ],</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF">            "temperature"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF">0.3</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        }</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8">        r </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8"> requests.post(url, </span><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70">headers</span><span style="--sdef build_dynamic_prompt():
    services, settings = get_clinic_data_from_sheet()
    
    base_prompt = f"""
أنت موظف استقبال ذكي لعيادة الدكتور عمار حسين الراوي.
تتحدث عراقي مهذب.

معلومات حية من Google Sheet (ID: {SHEET_ID}):
الخدمات والاسعار:
{services}

الاعدادات:
{settings}

قواعد:
1. ابدأ بـ: أهلاً وسهلاً بيك في عيادة الدكتور عمار حسين الراوي 🌿
2. اذا سأل عن سعر، خذه من الخدمات اعلاه
3. اذا سأل عن دوام او تواجد الدكاترة، خذه من الاعدادات اعلاه
4. لا تشخص طبيا ابدا
5. عند الحجز اطلب الاسم والوقت واحفظه
6. انهي بـ: دوامنا من 15:30-22:00 - الجمعة عطلة - 0780540459
"""
    return base_prompt

# ============ ارسال رسالة واتساب ============
def send_whatsapp(to, text):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}", "Content-Type": "application/json"}
    payload = {"messaging_product": "whatsapp", "to": to, "type": "text", "text": {"body": text}}
    requests.post(url, headers=headers, json=payload)

# ============ الذكاء الاصطناعي ============
def ask_ai(user_message):
    prompt = build_dynamic_prompt()
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "llama-3.1-70b-versatile",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.3
    }
    try:
        r = requests.post(url, headers=headers, json=data, timeout=20)
        return r.json()['choices'][0]['message']['content']
    except:
        return "أهلاً وسهلاً بيك 🌿 صار خلل بسيط، تكدر تتواصل على 0780540459 - دوامنا 3:30 عصراً للـ 10 مساءً"

# ============ حفظ الحجز في الشيت عن طريق Google Forms / Apps Script ============
# ضع هنا رابط الـ Web App اللي طلعلك من Apps Script
APPS_SCRIPT_WEBAPP_URL = "ضع_رابط_الويب_آب_هنا"

def save_booking_to_sheet(name, phone, time, service):
    import datetime
    data = {
        "date": str(datetime.date.today()),
        "time": time,
        "name": name,
        "phone": phone,
        "service": service,
        "doctor": "د. عمار"
    }
    try:
        requests.post(APPS_SCRIPT_WEBAPP_URL, json=data)
    except:
        pass

# مثال للتجربة المحلية
if __name__ == "__main__":
    print("البوت مربوط بالشيت:")
    print(f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")
    print("\nجرب سؤال:")
    print(ask_ai("شكد سعر زراعة السن؟"))
