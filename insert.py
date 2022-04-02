'''
Fake data for development purpose

Need to make sure the database schema is up to date
(with the `manage.py` file) before running this file.
'''


# Import all models from `models.py`
from models import *


# Data for Login model
Logins_to_add = [{
    'id': 1,
    'email': 'arshallat@uni.minerva.edu',
    'password': '',
}, {
    'id': 2,
    'email': 'dragoncy@uni.minerva.edu',
    'password': '',
}, {
    'id': 3,
    'email': 'elisha@uni.minerva.edu',
    'password': '',
}, {
    'id': 4,
    'email': 'theemskerk@uni.minerva.edu',
    'password': '',
}, {
    'id': 5,
    'email': 'abigail.gust@uni.minerva.edu',
    'password': '',
}, {
    'id': 6,
    'email': 'alya@uni.minerva.edu',
    'password': '',
}]


# Data for User model
Users_to_add = [{
    'id': 1,
    'login_id': 1,
    'firstname': 'Anna',
    'lastname': 'Shallat',
    'role': RoleEnum.student,
    'primary_major': CollegeEnum.AH,
    # 'secondary_major': '',
    'primary_concentration': ConcentrationEnum.AL,
    'secondary_concentration': ConcentrationEnum.PEL,
    # 'special_concentration': '',
    # 'minor': '',
    # 'minor_concentration': '',
}, {
    'id': 2,
    'login_id': 2,
    'firstname': 'Dragon',
    'lastname': 'Cruz-Yen',
    'role': RoleEnum.student,
    'primary_major': CollegeEnum.AH,
    # 'secondary_major': '',
    'primary_concentration': ConcentrationEnum.AL,
    # 'secondary_concentration': '',
    # 'special_concentration': '',
    'minor': CollegeEnum.SS,
    'minor_concentration': ConcentrationEnum.CBB,
}, {
    'id': 3,
    'login_id': 3,
    'firstname': 'Elisha',
    'lastname': 'Somasundram',
    'role': RoleEnum.student,
    'primary_major': CollegeEnum.AH,
    # 'secondary_major': '',
    'primary_concentration': ConcentrationEnum.AL,
    'secondary_concentration': ConcentrationEnum.PEL,
    # 'special_concentration': '',
    'minor': CollegeEnum.SS,
    'minor_concentration': ConcentrationEnum.CBB,
}, {
    'id': 4,
    'login_id': 4,
    'firstname': 'Tessa',
    'lastname': 'Heemskerk',
    'role': RoleEnum.student,
    'primary_major': CollegeEnum.AH,
    # 'secondary_major': '',
    'primary_concentration': ConcentrationEnum.AL,
    # 'secondary_concentration': '',
    # 'special_concentration': '',
    'minor': CollegeEnum.BS,
    # 'minor_concentration': '',
}, {
    'id': 5,
    'login_id': 5,
    'firstname': 'Abigail',
    'lastname': 'Gust',
    'role': RoleEnum.student,
    'primary_major': CollegeEnum.AH,
    # 'secondary_major': '',
    'primary_concentration': ConcentrationEnum.HAN,
    # 'secondary_concentration': '',
    # 'special_concentration': '',
    # 'minor': '',
    # 'minor_concentration': '',
}, {
    'id': 6,
    'login_id': 6,
    'firstname': 'Alya',
    'lastname': 'Luk',
    'role': RoleEnum.student,
    'primary_major': CollegeEnum.AH,
    'secondary_major': CollegeEnum.AH,
    'primary_concentration': ConcentrationEnum.HAP,
    'secondary_concentration': ConcentrationEnum.PEL,
    # 'special_concentration': '',
    'minor': CollegeEnum.CS,
    'minor_concentration': ConcentrationEnum.CSAI,
}]


# Data for Capstones model
Capstones_to_add = [{
    'id': 1,
    'user_id': 1,
    # 'advisor_id': '',
    'title': 'Zines and Queer Ethics',
    'abstract': 'This project will focus on how the ethical concerns of the LGBTQ+ community are promoted using the medium of zines. I intend accomplish four goals that build on each other, though there will be overlap between goals. First, I will identify the qualities of the medium that are conducive to moral and political persuasion. Second, I will consider how zines have historically amplified queer voices to promote positive change. Third, I will critique existing zines to identify their effective communication techniques. Finally, I will create a zine that promotes an ethical position. My intended deliverables are a literature review, critical analysis, ethical argument, and creative work.',
    'keywords': 'Zines, Ethics, LGBTQ+, subculture',
    # 'feature': [FeatureEnum.creative, FeatureEnum.secondary_research, FeatureEnum.philosophical],
    'los': '#ah144ethicaltheory, #ah146rupturesanddislocations, #ah166multimediaanalysis, #ah166protestart, #ah156artmarkets',
    # 'custom_los': '',
    'hsr_review': HSREnum.na,
}, {
    'id': 2,
    'user_id': 2,
    # 'advisor_id': '',
    'title': 'Raft: From Survival to Art',
    'abstract': 'The main idea of this project is to apply the lessons learned from the past couple of years to create an art project of professional quality and communicative power. My intended outcome for this project is to prepare myself for working as a full-time artist after finishing school. Guiding questions include ""What does it take to be a mainstream artist in the modern age?" and "what is success in art?". \n My intended deliverables include a full-length album of 10+ songs and an essay exploring the current mainstream hip hop industry. The album will be titled “Raft” and closely follow a distilled, fantastic version of my life focused on lessons learned through both joy and pain. On the other-hand, my accompanying paper will consider the benefits and drawbacks of mainstream hip hop success, proposing an alternative approach that prioritizes artist and audience. \n My approach centers around using the skills I have developed during this journey in producing, rapping, writing, singing, and research. I will work on both deliverables simultaneously."',
    'keywords': 'music, art, philosophy, humanity, film, creation, writing, recording, sampling, music theory, journey, life, learning, trauma, healing',
    # 'feature': [FeatureEnum.creative],
    'los': '#ah166musicalanalysis, #ah146artessay, #ah166contextualizeart, #ah156artmarkets, ah166expressart',
    # 'custom_los': '',
    'hsr_review': HSREnum.na,
}, {
    'id': 3,
    'user_id': 3,
    # 'advisor_id': '',
    'title': 'Museum Exhibit: Reimagining how Museums should curate art pieces from different cultures that authentically reflects their various attitudes towards art',
    'abstract': 'Our conceptions of art are largely informed by what we perceive to be art, and as artworks in museums are often the only access people have to some cultures, it is important that these works are presented authentically and representational and the culture it comes from.. As such, I will be discussing various conceptions of what art is and how it should be presented and experienced by an audience. \n For instance, considering what the purpose of art is, and how it ultimately expresses or communicates a meaning to a spectator (Dewey, 1934; Collingwood, 1939; Langer, 1943). I will be looking into how these theories of art are in accordance with art we see in museums. Finally, I will look into how differing cultural attitudes affect how we ought to view art, which will inform me on how I shall structure my museum exhibit (a deliverable alongside a research paper) to reimagine the way art is experienced.',
    'keywords': 'Museum, curation, cultural representation, aestheticism, philosophies of art',
    # 'feature': [FeatureEnum.creative, FeatureEnum.secondary_research, FeatureEnum.philosophical],
    'los': '#ah146-interpretingforms, #ah146-framingdisciplines, #ah146-rupturesanddislocations, #ah166-expressart, #ah166-contextualiseart, #ah166-produceart',
    'custom_los': '#culturalappropriation: Identifying when cultural appropriate has occurred as well as what underlying forces allow for this appropriation to persist',
    'hsr_review': HSREnum.na,
}, {
    'id': 4,
    'user_id': 4,
    # 'advisor_id': '',
    'title': "Crossing Over: Screenwriting and Narrative Film's Potential for Coping With and Healing Grief and Loss",
    'abstract': 'For my Capstone, I intend to generate a fiction feature film-length screenplay on the following premise: ‘Having lost their son in his attempt of crossing the Pacific by sailboat, a since-estranged couple decide to reattempt this journey together, having to not only overcome the physical challenges involved but also face the realities of grief in trying to reconnect with one another.’ This project intends not only to produce a compelling creative product but to explore the question of what lessons from theory on storytelling and its therapeutic potential can be applied to the creation of a screenplay that could employ the power of narrative film as a coping and healing tool for audiences dealing with hardship and loss in their own life. It will produce three deliverables: a literature review on storytelling and its therapeutic potential, a feature-length screenplay, and an accompanying analysis of the final product as well as the process and how it applies learned concepts or potentially led to further insights.',
    'keywords': 'Screenwriting, grief, storytelling, art and personal healing',
    # 'feature': [FeatureEnum.creative, FeatureEnum.secondary_research, FeatureEnum.other],
    'los': '#ah146artessay, #ah146readingsigns, #ah166litanalysis, #ah166expressart, #ah166produceart',
    'custom_los': '#screenplaytofilm: Evaluate the degree to which the written work of a screenplay utilizes the characteristics and tools that are particular to this medium to come together as a product that would translate well into an actual movie.',
    'hsr_review': HSREnum.na,
}, {
    'id': 5,
    'user_id': 5,
    # 'advisor_id': '',
    'title': 'Ruination of the Midwestern Barn: A Romanticization',
    'abstract': 'Every structure that remains in the landscape is a choice. Deliberate destruction, careful preservation, or allowance of the natural processes of decay are all decisions on what to keep from the relentless beating of time and what to submit to it. The current condition of the heartland’s farmsteads is widespread abandonment with deteriorating barns dotting the rural landscape with the frequency of Starbucks in suburban stripmalls. The response to this allowance of decay need not only be lamentation. We can allow ourselves to admire and even romanticize this decay. The preservationist instinct to save all would amount to an entombed, static world. \n This thesis will focus specifically on the deterioration of barns in Kane County Illinois, as well as an investigation into alternatives (museumification, repurposing) from local preservationist groups. There will be a photography and ‘driving tour of decay’ accompaniment. \n This project will apply concepts from European theorists and authors on ruins, typically centered on the Mediterranean, to a new context of contemporarily forsaken barns in rural Illinois. Two central thinkers are David Lowenthal’s ideas on heritage and the ‘continual refashioning’ of the past, and Rose Macaulay’s typology of ruin-pleasure.',
    'keywords': 'Rural ruins, decay, barns & farmsteads, architectural photography, archival work, heritage & preservation, nostalgia, ruin-pleasure',
    # 'feature': [FeatureEnum.creative, FeatureEnum.secondary_research, FeatureEnum.philosophical],
    'los': '#AH162historicalsources, #AH162publichistory, #AH152structureandagency, #AH110historicalsilences, #AH164implications',
    # 'custom_los': '',
    'hsr_review': HSREnum.na,
}, {
    'id': 6,
    'user_id': 6,
    # 'advisor_id': '',
    'title': 'Ethics of Gacha: Formulating an Ethical Guideline for Developers',
    'abstract': 'Abstract: This Capstone intends to discuss the ethical complexities seen in games that employ ‘Gacha’ mechanics—a system that involves purchasable randomised rewards. There is an increasing amount of legal and ethical concern for game mechanics like Gacha due to its likeness to gambling and ‘predatory’ design that appears to target at-risk users, particularly due to the popularity and unrestricted nature of such games. The project aims challenge these criticisms and to use an in-depth case study of the chart-topping Gacha game, Genshin Impact, to explore the real-world consequences of such mechanics, the ethical dilemmas they evoke on behalf of different parties (such as users who play for free, users who habitually monetise, the game developers, etc.), and how other mechanics and experiences in the game affect those outcomes. As a product of this analysis, the project aims to provide a framework for game companies to employ Gacha mechanics (and Gacha-related systems) in an ethical manner, building upon King and Delfabbro’s (2019) framework for loot box mechanics.',
    'keywords': 'business ethics, art ethics, game design',
    # 'feature': [FeatureEnum.creative, FeatureEnum.philosophical, FeatureEnum.policy],
    'los': '#ah154rights, #ah144ethicalconsiderations, #ah144ethicaljudgement, #ah144internationalethics, #ah166contextualizeart, #ah166multimedianalysis',
    # 'custom_los': '',
    'hsr_review': HSREnum.na,
}]

def insert_data():
    """To insert data"""

    # Create application context to add data to the database
    from app import create_app
    my_app = create_app()
    my_app.app_context().push()

    # List of keys with (list_of_data, model) to iterate
    keys = [(Logins_to_add, Login), (Users_to_add, User), (Capstones_to_add, Project)]

    # Insert data
    for dict_to_add, table in keys:
        for dict_row in dict_to_add:
            try:
                stmt = table(**dict_row)
                db.session.add(stmt)
                db.session.commit()
            except:
                db.session.rollback()
                raise
            finally:
                db.session.close()

insert_data()
