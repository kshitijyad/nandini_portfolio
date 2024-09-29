info = {
   "Pronoun": "her", 
   "Name": "Nandini",
   "Full_Name": "Nandini Comar",
   "Intro": "New York Registered Lawyer, with experince in Intellectual Property, Trademark, Contracts and Patents",
   "About":"Hi, I'm Nandini Comar, an experienced attorney specializing in commercial contracts and technology agreements. With 5+ years of experience, I've negotiated and drafted over 100 contracts, including software, SaaS, data license, and professional services agreements. I excel at developing strategic partnerships with business leaders, implementing best practices, and advising on complex legal issues and risks. My background includes managing IP portfolios for 25+ clients, reducing infringement incidents by 90%, and navigating patent litigation. I'm adept at translating complex legal concepts into clear, actionable insights for non-legal stakeholders, ensuring effective communication across teams. My experience in contract compliance, risk mitigation, and cross-functional collaboration makes me well-suited to support Moody's financial intelligence, data analytics, and software services businesses.",
   "City":"New York, United States",
   "Email": "comarnan@gmail.com"
}

embed_rss= {
    'rss':"""<div style="overflow-y: scroll; height:500px; background-color:white;"> <div id="retainable-rss-embed" 
        data-rss=""
        data-maxcols="3" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Read the rest" 
        data-buttonclass="btn btn-primary" 
        data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""
}

import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
endorsements = {
    "img1": image_to_base64("images/recommendation1.png"),
    "img2": image_to_base64("images/recommendation2.png"),
    "img3": image_to_base64("images/recommendation3.png")
}
