#!/usr/bin/env python3
"""
Lidice's Cleaning Services - Static Site Generator

Generates a bilingual (English/Swedish) static website for GitHub Pages.
Run: python3 generate_site.py
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# =============================================================================
# CONFIGURATION
# =============================================================================

OUTPUT_DIR = Path("docs")
FORMSPREE_ENDPOINT = "https://formspree.io/f/xyzgkqwp"  # Replace with actual endpoint

CONTACT_INFO = {
    'phone': '+46 73 534 4533',
    'email': 'lidice.cleaning@gmail.com',
    'hours': {
        'en': 'Mon-Fri 7:00-18:00',
        'sv': 'Man-Fre 7:00-18:00'
    },
    'location': 'Stockholm, Sweden'
}

# =============================================================================
# BILINGUAL CONTENT
# =============================================================================

CONTENT = {
    'en': {
        'lang_code': 'en',
        'lang_name': 'English',
        'lang_abbr': 'EN',
        'other_lang': 'sv',
        'other_abbr': 'SV',

        'nav': {
            'home': 'Home',
            'services': 'Services',
            'quote': 'Get Quote',
            'about': 'About Us'
        },

        'pages': {
            'home': 'index.html',
            'services': 'services.html',
            'quote': 'quote.html',
            'about': 'about.html'
        },

        'hero': {
            'title': "Professional Cleaning Services in Stockholm",
            'subtitle': "Eco-Friendly Residential and School Cleaning You Can Trust",
            'cta': "Get a Free Quote",
            'or_call': "Or call"
        },

        'stats': [
            {'number': '500+', 'label': 'Happy Clients'},
            {'number': '10+', 'label': 'Years Experience'},
            {'number': '100%', 'label': 'Green Products'},
            {'number': '24h', 'label': 'Response Time'}
        ],

        'how_it_works': {
            'title': "How It Works",
            'subtitle': "Getting started is simple",
            'steps': [
                {'number': '1', 'title': 'Request a Quote', 'desc': 'Fill out our form or call us. We will discuss your needs and schedule a free assessment.'},
                {'number': '2', 'title': 'Get Your Plan', 'desc': 'Receive a customized cleaning plan and transparent pricing within 24 hours.'},
                {'number': '3', 'title': 'Enjoy Clean Spaces', 'desc': 'Our trained professionals arrive on schedule with eco-friendly products.'}
            ]
        },

        'services_overview': {
            'title': "Our Services",
            'learn_more': "Learn more",
            'residential': {
                'title': "Residential Cleaning",
                'desc': "Keep your home spotless with our professional cleaning services using only eco-friendly, non-toxic products."
            },
            'school': {
                'title': "School Cleaning",
                'desc': "Safe, thorough cleaning for educational facilities from kindergarten to secondary school."
            }
        },

        'green_commitment': {
            'title': "100% Green Products",
            'subtitle': "Our Commitment to the Environment",
            'intro': "At Lidice's Cleaning Services, we exclusively use environmentally responsible cleaning products that are:",
            'points': [
                {
                    'title': "Non-Toxic",
                    'desc': "Safe for children, pets, and families. No harsh chemicals that compromise indoor air quality."
                },
                {
                    'title': "Biodegradable",
                    'desc': "Our products break down naturally without harming waterways or ecosystems."
                },
                {
                    'title': "Certified Eco-Friendly",
                    'desc': "We use products certified by Nordic Swan Ecolabel and EU Ecolabel standards."
                },
                {
                    'title': "Effective",
                    'desc': "Green does not mean less effective. Our products deliver professional-grade results."
                }
            ]
        },

        'testimonials': {
            'title': "Client Testimonials",
            'items': [
                {
                    'text': "We switched to Lidice's after learning about their green cleaning approach. Our home has never been cleaner, and we feel good knowing the products are safe for our children.",
                    'author': "Maria Svensson",
                    'role': "Homeowner",
                    'location': "Sodermalm, Stockholm"
                },
                {
                    'text': "As a school administrator, finding a cleaning service that prioritizes child safety was essential. Lidice's team uses only certified eco-friendly products, and the results speak for themselves.",
                    'author': "Erik Lindqvist",
                    'role': "Principal, Solstralens Forskola",
                    'location': "Kungsholmen, Stockholm"
                },
                {
                    'text': "Professional, punctual, and environmentally conscious. They transformed our office space while using products that do not aggravate allergies. Highly recommended.",
                    'author': "Anna Karlsson",
                    'role': "Office Manager",
                    'location': "Ostermalm, Stockholm"
                },
                {
                    'text': "After years of using conventional cleaning services, we made the switch to Lidice's. The difference in air quality alone was noticeable within the first week.",
                    'author': "Johan Berg",
                    'role': "Homeowner",
                    'location': "Vasastan, Stockholm"
                }
            ]
        },

        'trust_badges': {
            'title': "Why Choose Us",
            'badges': [
                {'title': "Licensed & Insured", 'desc': "Fully licensed business with comprehensive liability insurance for your peace of mind."},
                {'title': "Trained Professionals", 'desc': "Our team is trained in eco-friendly cleaning techniques and safety protocols."},
                {'title': "Satisfaction Guaranteed", 'desc': "Not happy? We will re-clean at no extra charge. Your satisfaction is our priority."},
                {'title': "Flexible Scheduling", 'desc': "Book at times that work for you. We accommodate your schedule, not the other way around."}
            ]
        },

        'faq': {
            'title': "Frequently Asked Questions",
            'items': [
                {'q': "What cleaning products do you use?", 'a': "We exclusively use Nordic Swan Ecolabel and EU Ecolabel certified products. All our cleaning solutions are non-toxic, biodegradable, and safe for children and pets."},
                {'q': "How do I get a quote?", 'a': "Fill out our online form or call us directly. We will discuss your needs and provide a free, no-obligation quote within 24 hours."},
                {'q': "Do you bring your own equipment?", 'a': "Yes, we bring all necessary cleaning equipment and eco-friendly products. You do not need to provide anything."},
                {'q': "What areas in Stockholm do you serve?", 'a': "We serve all of greater Stockholm including Sodermalm, Ostermalm, Kungsholmen, Vasastan, Norrmalm, Sundbyberg, Solna, Nacka, and Lidingo."},
                {'q': "Can I request the same cleaner each time?", 'a': "Yes, we prioritize consistency. Once you are matched with a cleaner you like, we do our best to send the same person for all your appointments."},
                {'q': "What is your cancellation policy?", 'a': "We ask for 24 hours notice for cancellations or rescheduling. This helps us maintain efficient scheduling for all our clients."}
            ]
        },

        'cta_section': {
            'title': "Ready for a Cleaner, Greener Space?",
            'subtitle': "Get your free, no-obligation quote today",
            'button': "Request Quote"
        },

        'footer': {
            'tagline': "Eco-Friendly Professional Cleaning in Stockholm",
            'contact': "Contact Us",
            'hours': "Business Hours",
            'quick_links': "Quick Links",
            'follow_us': "Follow Us",
            'copyright': f"© {datetime.now().year} Lidice's Cleaning Services. All rights reserved."
        },

        'cookie': {
            'message': "We use cookies to improve your experience on our website.",
            'accept': "Accept",
            'decline': "Decline",
            'link_text': "Privacy Policy"
        },

        # Services Page
        'services_page': {
            'title': "Our Services",
            'subtitle': "Professional eco-friendly cleaning solutions for homes and schools",
            'green_note': "All services use 100% eco-friendly, non-toxic cleaning products",
            'residential': {
                'title': "Residential Cleaning",
                'intro': "Transform your home into a spotless sanctuary with our comprehensive residential cleaning services. Every product we use is safe for your family and the environment.",
                'services': [
                    {
                        'name': "Regular Cleaning",
                        'desc': "Weekly or bi-weekly cleaning to maintain your home. Includes dusting, vacuuming, mopping, bathroom and kitchen cleaning with eco-certified products."
                    },
                    {
                        'name': "Deep Cleaning",
                        'desc': "Thorough top-to-bottom cleaning including hard-to-reach areas, behind furniture, inside appliances, and detailed sanitization using green products."
                    },
                    {
                        'name': "Move-In/Move-Out Cleaning",
                        'desc': "Complete cleaning service for empty properties. Perfect for tenants, landlords, and real estate agents requiring professional results."
                    },
                    {
                        'name': "Window Cleaning",
                        'desc': "Crystal clear windows inside and out using streak-free, environmentally safe solutions. We handle all window types including frames and sills."
                    }
                ]
            },
            'school': {
                'title': "School Cleaning",
                'intro': "Creating safe, healthy learning environments for students of all ages. Our specialized educational facility cleaning uses only child-safe, certified green products.",
                'services': [
                    {
                        'name': "Kindergarten (Forskola)",
                        'desc': "Child-safe cleaning with non-toxic products. Special attention to play areas, toys, and surfaces children touch daily."
                    },
                    {
                        'name': "Primary School (Grundskola)",
                        'desc': "Daily classroom maintenance, hallway cleaning, cafeteria sanitization, and bathroom hygiene using eco-certified products."
                    },
                    {
                        'name': "Secondary School (Gymnasium)",
                        'desc': "Comprehensive cleaning for larger facilities including laboratories, gymnasiums, locker rooms, and common areas."
                    },
                    {
                        'name': "Deep Sanitization",
                        'desc': "Intensive cleaning during holidays and breaks. Includes carpet cleaning, floor polishing, and complete disinfection with green products."
                    }
                ]
            }
        },

        # Quote Page
        'quote_page': {
            'title': "Get a Free Quote",
            'subtitle': "Fill out the form below and we will respond within 24 hours",
            'form': {
                'service_type': "Select Service Type",
                'residential_label': "Residential",
                'residential_desc': "Home cleaning services",
                'school_label': "School",
                'school_desc': "Educational facility cleaning",
                'specific_service': "Specific Service (optional)",
                'service_placeholder': "e.g., Deep cleaning, Window cleaning, Move-out...",
                'contact_details': "Your Contact Information",
                'property_details': "Property Details",
                'property_size': "Property Size (sqm)",
                'size_placeholder': "e.g., 80",
                'frequency': "How Often?",
                'freq_onetime': "One-time",
                'freq_weekly': "Weekly",
                'freq_biweekly': "Bi-weekly",
                'freq_monthly': "Monthly",
                'freq_custom': "Custom",
                'name': "Full Name",
                'email': "Email Address",
                'phone': "Phone Number",
                'phone_placeholder': "+46 XX XXX XXXX",
                'address': "Property Address",
                'address_placeholder': "Street, City",
                'message': "Additional Information",
                'message_placeholder': "Tell us about any special requirements, access instructions, or questions...",
                'submit': "Send Quote Request",
                'privacy': "Your information is secure and will only be used to respond to your inquiry."
            },
            'next_steps': {
                'title': "What Happens Next?",
                'step1_title': "We Review",
                'step1_desc': "Our team reviews your request and prepares a customized quote.",
                'step2_title': "We Contact You",
                'step2_desc': "Within 24 hours, we will call or email with your detailed quote.",
                'step3_title': "You Decide",
                'step3_desc': "No pressure. Review the quote and let us know if you would like to proceed."
            },
            'prefer_call': {
                'title': "Prefer to Talk?",
                'desc': "Call us directly and speak with our team."
            },
            'trust': {
                'free': "Free Quote",
                'response': "24h Response",
                'obligation': "No Obligation"
            },
            'success': "Thank you! We will contact you within 24 hours.",
            'error': "Something went wrong. Please try again or call us directly."
        },

        # About Page
        'about_page': {
            'title': "About Lidice's Cleaning Services",
            'subtitle': "Your trusted eco-friendly cleaning partner in Stockholm",
            'story': {
                'title': "Our Story",
                'paragraphs': [
                    "Lidice's Cleaning Services was founded with a commitment to providing Stockholm homes and schools with cleaning services that are both effective and environmentally responsible.",
                    "We believe that a truly clean environment should not come at the cost of your health or the planet. That is why we exclusively use eco-certified, non-toxic cleaning products that deliver professional results without harmful chemicals.",
                    "Our team of trained professionals treats every space with care and attention to detail, ensuring consistent quality while maintaining our green standards."
                ]
            },
            'values': {
                'title': "Our Values",
                'items': [
                    {
                        'title': "Environmental Responsibility",
                        'desc': "We use only certified eco-friendly products. Our commitment to green cleaning is non-negotiable."
                    },
                    {
                        'title': "Quality",
                        'desc': "We never compromise on results. Every job meets our high professional standards."
                    },
                    {
                        'title': "Reliability",
                        'desc': "Count on us to arrive on time, every time. We respect your schedule and commitments."
                    },
                    {
                        'title': "Transparency",
                        'desc': "Clear pricing, honest communication, and no hidden fees. What we quote is what you pay."
                    }
                ]
            },
            'service_area': {
                'title': "Service Area",
                'desc': "We proudly serve the greater Stockholm area including:",
                'areas': ["Stockholm City", "Sodermalm", "Ostermalm", "Kungsholmen", "Vasastan", "Norrmalm", "Sundbyberg", "Solna", "Nacka", "Lidingo"]
            }
        }
    },

    'sv': {
        'lang_code': 'sv',
        'lang_name': 'Svenska',
        'lang_abbr': 'SV',
        'other_lang': 'en',
        'other_abbr': 'EN',

        'nav': {
            'home': 'Hem',
            'services': 'Tjanster',
            'quote': 'Fa Offert',
            'about': 'Om Oss'
        },

        'pages': {
            'home': 'index.html',
            'services': 'tjanster.html',
            'quote': 'offert.html',
            'about': 'om-oss.html'
        },

        'hero': {
            'title': "Professionella Stadtjanster i Stockholm",
            'subtitle': "Miljovanlig Hem- och Skolstadning Du Kan Lita Pa",
            'cta': "Fa en Gratis Offert",
            'or_call': "Eller ring"
        },

        'stats': [
            {'number': '500+', 'label': 'Nojda Kunder'},
            {'number': '10+', 'label': 'Ars Erfarenhet'},
            {'number': '100%', 'label': 'Grona Produkter'},
            {'number': '24h', 'label': 'Svarstid'}
        ],

        'how_it_works': {
            'title': "Sa Har Fungerar Det",
            'subtitle': "Att komma igang ar enkelt",
            'steps': [
                {'number': '1', 'title': 'Begar Offert', 'desc': 'Fyll i vart formular eller ring oss. Vi diskuterar dina behov och bokar en kostnadsfri bedomning.'},
                {'number': '2', 'title': 'Fa Din Plan', 'desc': 'Fa en skraddarsydd stadplan och transparent prissattning inom 24 timmar.'},
                {'number': '3', 'title': 'Njut av Rena Utrymmen', 'desc': 'Vara utbildade proffs kommer enligt schema med miljovanliga produkter.'}
            ]
        },

        'services_overview': {
            'title': "Vara Tjanster",
            'learn_more': "Las mer",
            'residential': {
                'title': "Hemstadning",
                'desc': "Hall ditt hem skinande rent med vara professionella stadtjanster som endast anvander miljovanliga, giftfria produkter."
            },
            'school': {
                'title': "Skolstadning",
                'desc': "Saker, grundlig stadning for utbildningsanlaggningar fran forskola till gymnasium."
            }
        },

        'green_commitment': {
            'title': "100% Grona Produkter",
            'subtitle': "Vart Miljoatagande",
            'intro': "Pa Lidice's Cleaning Services anvander vi uteslutande miljoansvariga stadprodukter som ar:",
            'points': [
                {
                    'title': "Giftfria",
                    'desc': "Sakra for barn, husdjur och familjer. Inga starka kemikalier som forsamrar inomhusluften."
                },
                {
                    'title': "Biologiskt Nedbrytbara",
                    'desc': "Vara produkter bryts ner naturligt utan att skada vattendrag eller ekosystem."
                },
                {
                    'title': "Certifierat Miljovanliga",
                    'desc': "Vi anvander produkter certifierade enligt Svanen och EU Ecolabel-standarder."
                },
                {
                    'title': "Effektiva",
                    'desc': "Gront betyder inte mindre effektivt. Vara produkter levererar professionella resultat."
                }
            ]
        },

        'testimonials': {
            'title': "Kundrecensioner",
            'items': [
                {
                    'text': "Vi bytte till Lidice's efter att ha lart oss om deras grona stadmetod. Vart hem har aldrig varit renare, och vi kanner oss trygga med att produkterna ar sakra for vara barn.",
                    'author': "Maria Svensson",
                    'role': "Villaagare",
                    'location': "Sodermalm, Stockholm"
                },
                {
                    'text': "Som skoladministrator var det viktigt att hitta en stadtjanst som prioriterar barnsaker. Lidice's team anvander endast certifierade miljovanliga produkter, och resultaten talar for sig sjalva.",
                    'author': "Erik Lindqvist",
                    'role': "Rektor, Solstralens Forskola",
                    'location': "Kungsholmen, Stockholm"
                },
                {
                    'text': "Professionella, punktliga och miljomedvetna. De forvandlade vart kontorsutrymme medan de anvande produkter som inte forvarrar allergier. Rekommenderas varmt.",
                    'author': "Anna Karlsson",
                    'role': "Kontorschef",
                    'location': "Ostermalm, Stockholm"
                },
                {
                    'text': "Efter ar av att anvanda konventionella stadtjanster gjorde vi bytet till Lidice's. Skillnaden i luftkvalitet ensam var marktbar inom forsta veckan.",
                    'author': "Johan Berg",
                    'role': "Villaagare",
                    'location': "Vasastan, Stockholm"
                }
            ]
        },

        'trust_badges': {
            'title': "Varfor Valja Oss",
            'badges': [
                {'title': "Licensierad & Forsakrad", 'desc': "Fullt licensierat foretag med omfattande ansvarsforsakring for din trygghet."},
                {'title': "Utbildade Proffs", 'desc': "Vart team ar utbildat i miljovanliga stadtekniker och sakerhetsprotokoll."},
                {'title': "Nojdhetsgaranti", 'desc': "Inte nojd? Vi stadar om utan extra kostnad. Din tillfredsstallelse ar var prioritet."},
                {'title': "Flexibel Bokning", 'desc': "Boka tider som passar dig. Vi anpassar oss efter ditt schema, inte tvartom."}
            ]
        },

        'faq': {
            'title': "Vanliga Fragor",
            'items': [
                {'q': "Vilka stadprodukter anvander ni?", 'a': "Vi anvander uteslutande Svanen och EU Ecolabel-certifierade produkter. Alla vara stadlosningar ar giftfria, biologiskt nedbrytbara och sakra for barn och husdjur."},
                {'q': "Hur far jag en offert?", 'a': "Fyll i vart onlineformular eller ring oss direkt. Vi diskuterar dina behov och ger en kostnadsfri offert inom 24 timmar."},
                {'q': "Tar ni med egen utrustning?", 'a': "Ja, vi tar med all nodvandig stadutrustning och miljovanliga produkter. Du behover inte tillhandahalla nagot."},
                {'q': "Vilka omraden i Stockholm betjanar ni?", 'a': "Vi betjanar hela Storstockholm inklusive Sodermalm, Ostermalm, Kungsholmen, Vasastan, Norrmalm, Sundbyberg, Solna, Nacka och Lidingo."},
                {'q': "Kan jag begar samma stadare varje gang?", 'a': "Ja, vi prioriterar kontinuitet. Nar du matchats med en stadare du gillar gor vi vart basta for att skicka samma person till alla dina bokningar."},
                {'q': "Vad ar er avbokningspolicy?", 'a': "Vi ber om 24 timmars varsel for avbokningar eller ombokningar. Detta hjalper oss att uppratthalla effektiv schemaplanering for alla vara kunder."}
            ]
        },

        'cta_section': {
            'title': "Redo for ett Renare, Gronare Utrymme?",
            'subtitle': "Fa din kostnadsfria offert idag",
            'button': "Begar Offert"
        },

        'footer': {
            'tagline': "Miljovanlig Professionell Stadning i Stockholm",
            'contact': "Kontakta Oss",
            'hours': "Oppettider",
            'quick_links': "Snabblankar",
            'follow_us': "Folj Oss",
            'copyright': f"© {datetime.now().year} Lidice's Cleaning Services. Alla rattigheter forbehallna."
        },

        'cookie': {
            'message': "Vi anvander cookies for att forbattra din upplevelse pa var webbplats.",
            'accept': "Acceptera",
            'decline': "Avboj",
            'link_text': "Integritetspolicy"
        },

        # Services Page
        'services_page': {
            'title': "Vara Tjanster",
            'subtitle': "Professionella miljovanliga stadlosningar for hem och skolor",
            'green_note': "Alla tjanster anvander 100% miljovanliga, giftfria stadprodukter",
            'residential': {
                'title': "Hemstadning",
                'intro': "Forvandla ditt hem till en skinande ren oas med vara omfattande hemstadningstjanster. Varje produkt vi anvander ar saker for din familj och miljon.",
                'services': [
                    {
                        'name': "Regelbunden Stadning",
                        'desc': "Veckovis eller varannan vecka stadning for att halla ditt hem rent. Inkluderar dammsugning, moppning, badrum och koksrengoring med miljocertifierade produkter."
                    },
                    {
                        'name': "Storstadning",
                        'desc': "Grundlig stadning fran topp till botten inklusive svaratkomliga omraden, bakom mobler, inuti vitvaror och detaljerad sanering med grona produkter."
                    },
                    {
                        'name': "Flytt-Stadning",
                        'desc': "Komplett stadservice for tomma bostader. Perfekt for hyresgaster, hyresvardar och fastighetsmaklare som kraver professionella resultat."
                    },
                    {
                        'name': "Fonsterputs",
                        'desc': "Kristallklara fonster bade invandigt och utvandigt med strimmfria, miljovanliga losningar. Vi hanterar alla fonstertyper inklusive karmar."
                    }
                ]
            },
            'school': {
                'title': "Skolstadning",
                'intro': "Skapar sakra, halsosamma larmiljoer for elever i alla aldrar. Var specialiserade stadning av utbildningsanlaggningar anvander endast barnsakra, certifierade grona produkter.",
                'services': [
                    {
                        'name': "Forskola",
                        'desc': "Barnsaker stadning med giftfria produkter. Sarskild uppmarksamhet pa lekomraden, leksaker och ytor som barn ror dagligen."
                    },
                    {
                        'name': "Grundskola",
                        'desc': "Dagligt underhall av klassrum, korridorstadning, matsalsanering och badrumshygien med miljocertifierade produkter."
                    },
                    {
                        'name': "Gymnasium",
                        'desc': "Omfattande stadning for storre anlaggningar inklusive laboratorier, gym, omkladningsrum och gemensamma utrymmen."
                    },
                    {
                        'name': "Djupdesinfektion",
                        'desc': "Intensiv stadning under lov och ledigheter. Inkluderar mattstadning, golvpolering och fullstandig desinfektion med grona produkter."
                    }
                ]
            }
        },

        # Quote Page
        'quote_page': {
            'title': "Fa en Gratis Offert",
            'subtitle': "Fyll i formularet nedan sa aterkommer vi inom 24 timmar",
            'form': {
                'service_type': "Valj Tjanstetyp",
                'residential_label': "Hemstadning",
                'residential_desc': "Stadtjanster for hemmet",
                'school_label': "Skola",
                'school_desc': "Stadning av utbildningslokaler",
                'specific_service': "Specifik Tjanst (valfritt)",
                'service_placeholder': "t.ex. Storstadning, Fonsterputs, Flyttstadning...",
                'contact_details': "Din Kontaktinformation",
                'property_details': "Fastighetsdetaljer",
                'property_size': "Storlek (kvm)",
                'size_placeholder': "t.ex. 80",
                'frequency': "Hur Ofta?",
                'freq_onetime': "Engangs",
                'freq_weekly': "Varje vecka",
                'freq_biweekly': "Varannan vecka",
                'freq_monthly': "Manadsvis",
                'freq_custom': "Anpassat",
                'name': "Fullstandigt Namn",
                'email': "E-postadress",
                'phone': "Telefonnummer",
                'phone_placeholder': "+46 XX XXX XXXX",
                'address': "Fastighetens Adress",
                'address_placeholder': "Gata, Stad",
                'message': "Ytterligare Information",
                'message_placeholder': "Beratta om specialkrav, tillgangsinstruktioner eller fragor...",
                'submit': "Skicka Offertforfragan",
                'privacy': "Din information ar saker och anvands endast for att svara pa din forfragan."
            },
            'next_steps': {
                'title': "Vad Hander Sedan?",
                'step1_title': "Vi Granskar",
                'step1_desc': "Vart team granskar din forfragan och forbereder en anpassad offert.",
                'step2_title': "Vi Kontaktar Dig",
                'step2_desc': "Inom 24 timmar ringer eller mejlar vi med din detaljerade offert.",
                'step3_title': "Du Bestammer",
                'step3_desc': "Ingen press. Granska offerten och meddela oss om du vill ga vidare."
            },
            'prefer_call': {
                'title': "Foredrar du att Prata?",
                'desc': "Ring oss direkt och prata med vart team."
            },
            'trust': {
                'free': "Gratis Offert",
                'response': "24h Svar",
                'obligation': "Ingen Forpliktelse"
            },
            'success': "Tack! Vi kontaktar dig inom 24 timmar.",
            'error': "Nagot gick fel. Forsok igen eller ring oss direkt."
        },

        # About Page
        'about_page': {
            'title': "Om Lidice's Cleaning Services",
            'subtitle': "Din betrodda miljovanliga stadpartner i Stockholm",
            'story': {
                'title': "Var Historia",
                'paragraphs': [
                    "Lidice's Cleaning Services grundades med ett atagande att forse Stockholms hem och skolor med stadtjanster som ar bade effektiva och miljoansvariga.",
                    "Vi tror att en verkligt ren miljo inte ska komma pa bekostnad av din halsa eller planeten. Darfor anvander vi uteslutande miljocertifierade, giftfria stadprodukter som levererar professionella resultat utan skadliga kemikalier.",
                    "Vart team av utbildade proffs behandlar varje utrymme med omsorg och uppmarksamhet pa detaljer, vilket garanterar konsekvent kvalitet samtidigt som vi uppratthaller vara grona standarder."
                ]
            },
            'values': {
                'title': "Vara Varderingar",
                'items': [
                    {
                        'title': "Miljoansvar",
                        'desc': "Vi anvander endast certifierade miljovanliga produkter. Vart atagande for gron stadning ar icke-forhandlingsbart."
                    },
                    {
                        'title': "Kvalitet",
                        'desc': "Vi kompromissar aldrig med resultat. Varje jobb uppfyller vara hoga professionella standarder."
                    },
                    {
                        'title': "Palitlighet",
                        'desc': "Rakna med att vi kommer i tid, varje gang. Vi respekterar ditt schema och dina ataganden."
                    },
                    {
                        'title': "Transparens",
                        'desc': "Tydlig prissattning, arlig kommunikation och inga dolda avgifter. Det vi offererar ar vad du betalar."
                    }
                ]
            },
            'service_area': {
                'title': "Serviceomrade",
                'desc': "Vi betjanar stolt Storstockholmsomradet inklusive:",
                'areas': ["Stockholms stad", "Sodermalm", "Ostermalm", "Kungsholmen", "Vasastan", "Norrmalm", "Sundbyberg", "Solna", "Nacka", "Lidingo"]
            }
        }
    }
}

# =============================================================================
# HTML TEMPLATES
# =============================================================================

def get_base_template(lang, title, content, active_page='home'):
    """Generate base HTML template with header and footer."""
    c = CONTENT[lang]
    other_lang = c['other_lang']

    # Determine the equivalent page in other language
    page_mapping = {
        'index.html': 'index.html',
        'services.html': 'tjanster.html',
        'tjanster.html': 'services.html',
        'quote.html': 'offert.html',
        'offert.html': 'quote.html',
        'about.html': 'om-oss.html',
        'om-oss.html': 'about.html'
    }
    current_page = c['pages'][active_page]
    other_page = page_mapping.get(current_page, 'index.html')

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Eco-friendly professional cleaning services in Stockholm. 100% green products. Residential and school cleaning.">
    <meta name="keywords" content="eco-friendly cleaning, green cleaning, Stockholm, hemstadning, skolstadning, miljovanlig stadning">
    <title>{title} | Lidice's Cleaning Services</title>

    <!-- Open Graph -->
    <meta property="og:title" content="{title} | Lidice's Cleaning Services">
    <meta property="og:description" content="Eco-friendly professional cleaning services in Stockholm using 100% green products.">
    <meta property="og:type" content="website">

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="../images/favicon.svg">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Styles -->
    <link rel="stylesheet" href="../css/style.css">

    <!-- Schema.org LocalBusiness -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Lidice's Cleaning Services",
        "description": "Eco-friendly professional cleaning services in Stockholm using 100% green products.",
        "url": "https://cubreto.github.io/lidice-cleaning/",
        "telephone": "{CONTACT_INFO['phone']}",
        "email": "{CONTACT_INFO['email']}",
        "address": {{
            "@type": "PostalAddress",
            "addressLocality": "Stockholm",
            "addressCountry": "SE"
        }},
        "openingHours": "Mo-Fr 07:00-18:00",
        "priceRange": "$$",
        "serviceArea": {{
            "@type": "City",
            "name": "Stockholm"
        }}
    }}
    </script>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <nav class="nav">
                <a href="{c['pages']['home']}" class="logo">
                    <span class="logo-text">Lidice's Cleaning</span>
                </a>

                <ul class="nav-links">
                    <li><a href="{c['pages']['home']}" class="{'active' if active_page == 'home' else ''}">{c['nav']['home']}</a></li>
                    <li><a href="{c['pages']['services']}" class="{'active' if active_page == 'services' else ''}">{c['nav']['services']}</a></li>
                    <li><a href="{c['pages']['quote']}" class="{'active' if active_page == 'quote' else ''}">{c['nav']['quote']}</a></li>
                    <li><a href="{c['pages']['about']}" class="{'active' if active_page == 'about' else ''}">{c['nav']['about']}</a></li>
                </ul>

                <div class="nav-actions">
                    <a href="../{other_lang}/{other_page}" class="lang-switch" title="{CONTENT[other_lang]['lang_name']}">
                        {c['other_abbr']}
                    </a>
                    <a href="{c['pages']['quote']}" class="btn btn-primary btn-sm">{c['nav']['quote']}</a>
                    <button class="mobile-menu-btn" aria-label="Menu">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </div>
            </nav>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <ul class="mobile-nav-links">
            <li><a href="{c['pages']['home']}">{c['nav']['home']}</a></li>
            <li><a href="{c['pages']['services']}">{c['nav']['services']}</a></li>
            <li><a href="{c['pages']['quote']}">{c['nav']['quote']}</a></li>
            <li><a href="{c['pages']['about']}">{c['nav']['about']}</a></li>
            <li><a href="../{other_lang}/{other_page}">{CONTENT[other_lang]['lang_name']}</a></li>
        </ul>
    </div>

    <!-- Main Content -->
    <main>
        {content}
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="{c['pages']['home']}" class="logo">
                        <span class="logo-text">Lidice's Cleaning</span>
                    </a>
                    <p>{c['footer']['tagline']}</p>
                </div>

                <div class="footer-contact">
                    <h4>{c['footer']['contact']}</h4>
                    <ul>
                        <li><a href="tel:{CONTACT_INFO['phone']}">{CONTACT_INFO['phone']}</a></li>
                        <li><a href="mailto:{CONTACT_INFO['email']}">{CONTACT_INFO['email']}</a></li>
                        <li>{CONTACT_INFO['location']}</li>
                    </ul>
                </div>

                <div class="footer-hours">
                    <h4>{c['footer']['hours']}</h4>
                    <p>{CONTACT_INFO['hours'][lang]}</p>
                </div>

                <div class="footer-links">
                    <h4>{c['footer']['quick_links']}</h4>
                    <ul>
                        <li><a href="{c['pages']['home']}">{c['nav']['home']}</a></li>
                        <li><a href="{c['pages']['services']}">{c['nav']['services']}</a></li>
                        <li><a href="{c['pages']['quote']}">{c['nav']['quote']}</a></li>
                        <li><a href="{c['pages']['about']}">{c['nav']['about']}</a></li>
                    </ul>
                </div>

                <div class="footer-social">
                    <h4>{c['footer']['follow_us']}</h4>
                    <div class="social-links">
                        <a href="#" class="social-link" aria-label="Facebook" title="Facebook">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                        </a>
                        <a href="#" class="social-link" aria-label="Instagram" title="Instagram">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
                        </a>
                        <a href="#" class="social-link" aria-label="LinkedIn" title="LinkedIn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
                        </a>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <p>{c['footer']['copyright']}</p>
            </div>
        </div>
    </footer>

    <!-- Cookie Consent Banner -->
    <div class="cookie-banner" id="cookie-banner">
        <div class="cookie-content">
            <p>{c['cookie']['message']}</p>
            <div class="cookie-actions">
                <button class="cookie-btn cookie-accept" id="cookie-accept">{c['cookie']['accept']}</button>
                <button class="cookie-btn cookie-decline" id="cookie-decline">{c['cookie']['decline']}</button>
            </div>
        </div>
    </div>

    <!-- Back to Top Button -->
    <button class="back-to-top" aria-label="Back to top">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="18 15 12 9 6 15"></polyline>
        </svg>
    </button>

    <script src="../js/main.js"></script>
</body>
</html>'''


def generate_home_page(lang):
    """Generate home page content."""
    c = CONTENT[lang]

    # Stats HTML
    stats_html = ''
    for s in c['stats']:
        stats_html += f'''
            <div class="stat-item">
                <span class="stat-number">{s['number']}</span>
                <span class="stat-label">{s['label']}</span>
            </div>'''

    # How it works HTML
    steps_html = ''
    for step in c['how_it_works']['steps']:
        steps_html += f'''
            <div class="step-card">
                <div class="step-number">{step['number']}</div>
                <h3>{step['title']}</h3>
                <p>{step['desc']}</p>
            </div>'''

    # Testimonials HTML
    testimonials_html = ''
    for t in c['testimonials']['items']:
        testimonials_html += f'''
            <div class="testimonial-card">
                <p class="testimonial-text">"{t['text']}"</p>
                <div class="testimonial-author">
                    <strong>{t['author']}</strong>
                    <span class="testimonial-role">{t['role']}</span>
                    <span class="testimonial-location">{t['location']}</span>
                </div>
            </div>'''

    # Green commitment points HTML
    green_points_html = ''
    for p in c['green_commitment']['points']:
        green_points_html += f'''
            <div class="green-point">
                <h3>{p['title']}</h3>
                <p>{p['desc']}</p>
            </div>'''

    # Trust badges HTML
    trust_badges_html = ''
    for b in c['trust_badges']['badges']:
        trust_badges_html += f'''
            <div class="trust-badge">
                <h3>{b['title']}</h3>
                <p>{b['desc']}</p>
            </div>'''

    # FAQ HTML
    faq_html = ''
    for i, item in enumerate(c['faq']['items']):
        faq_html += f'''
            <div class="faq-item">
                <button class="faq-question" aria-expanded="false" aria-controls="faq-{i}">
                    <span>{item['q']}</span>
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-answer" id="faq-{i}">
                    <p>{item['a']}</p>
                </div>
            </div>'''

    content = f'''
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <div class="hero-grid">
                    <div class="hero-content">
                        <h1>{c['hero']['title']}</h1>
                        <p class="hero-subtitle">{c['hero']['subtitle']}</p>
                        <div class="hero-actions">
                            <a href="{c['pages']['quote']}" class="btn btn-primary btn-lg">{c['hero']['cta']}</a>
                            <p class="hero-phone">{c['hero']['or_call']} <a href="tel:{CONTACT_INFO['phone']}">{CONTACT_INFO['phone']}</a></p>
                        </div>
                    </div>
                    <div class="hero-illustration">
                        <svg viewBox="0 0 400 300" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <!-- House -->
                            <path d="M200 40L320 120V260H80V120L200 40Z" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
                            <path d="M200 40L80 120H320L200 40Z" fill="#bbf7d0"/>
                            <!-- Door -->
                            <rect x="175" y="180" width="50" height="80" fill="#16a34a" rx="4"/>
                            <circle cx="215" cy="220" r="4" fill="#fbbf24"/>
                            <!-- Windows -->
                            <rect x="105" y="140" width="45" height="50" fill="#bfdbfe" stroke="#16a34a" stroke-width="2" rx="2"/>
                            <rect x="250" y="140" width="45" height="50" fill="#bfdbfe" stroke="#16a34a" stroke-width="2" rx="2"/>
                            <line x1="127" y1="140" x2="127" y2="190" stroke="#16a34a" stroke-width="2"/>
                            <line x1="105" y1="165" x2="150" y2="165" stroke="#16a34a" stroke-width="2"/>
                            <line x1="272" y1="140" x2="272" y2="190" stroke="#16a34a" stroke-width="2"/>
                            <line x1="250" y1="165" x2="295" y2="165" stroke="#16a34a" stroke-width="2"/>
                            <!-- Sparkles -->
                            <path d="M340 80L345 95L360 100L345 105L340 120L335 105L320 100L335 95L340 80Z" fill="#fbbf24"/>
                            <path d="M60 140L63 150L73 153L63 156L60 166L57 156L47 153L57 150L60 140Z" fill="#fbbf24"/>
                            <path d="M350 180L352 186L358 188L352 190L350 196L348 190L342 188L348 186L350 180Z" fill="#fbbf24"/>
                            <!-- Plant/Tree -->
                            <ellipse cx="50" cy="250" rx="30" ry="35" fill="#22c55e"/>
                            <rect x="45" y="250" width="10" height="30" fill="#92400e"/>
                            <!-- Cleaning bubbles -->
                            <circle cx="360" cy="240" r="12" fill="#dbeafe" stroke="#3b82f6" stroke-width="1"/>
                            <circle cx="345" cy="255" r="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="1"/>
                            <circle cx="370" cy="265" r="6" fill="#dbeafe" stroke="#3b82f6" stroke-width="1"/>
                        </svg>
                    </div>
                </div>
            </div>
        </section>

        <!-- Stats Bar -->
        <section class="stats-bar">
            <div class="container">
                <div class="stats-grid">
                    {stats_html}
                </div>
            </div>
        </section>

        <!-- Services Overview -->
        <section class="section services-overview">
            <div class="container">
                <h2 class="section-title">{c['services_overview']['title']}</h2>
                <div class="services-grid">
                    <a href="{c['pages']['services']}" class="service-card">
                        <h3>{c['services_overview']['residential']['title']}</h3>
                        <p>{c['services_overview']['residential']['desc']}</p>
                        <span class="card-link">{c['services_overview']['learn_more']}</span>
                    </a>
                    <a href="{c['pages']['services']}" class="service-card">
                        <h3>{c['services_overview']['school']['title']}</h3>
                        <p>{c['services_overview']['school']['desc']}</p>
                        <span class="card-link">{c['services_overview']['learn_more']}</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- How It Works -->
        <section class="section how-it-works">
            <div class="container">
                <h2 class="section-title">{c['how_it_works']['title']}</h2>
                <p class="section-subtitle">{c['how_it_works']['subtitle']}</p>
                <div class="steps-grid">
                    {steps_html}
                </div>
            </div>
        </section>

        <!-- Green Commitment -->
        <section class="section section-green green-section">
            <div class="container">
                <h2 class="section-title">{c['green_commitment']['title']}</h2>
                <p class="section-subtitle">{c['green_commitment']['subtitle']}</p>
                <p class="green-intro">{c['green_commitment']['intro']}</p>
                <div class="green-points-grid">
                    {green_points_html}
                </div>
            </div>
        </section>

        <!-- Testimonials -->
        <section class="section testimonials-section">
            <div class="container">
                <h2 class="section-title">{c['testimonials']['title']}</h2>
                <div class="testimonials-grid">
                    {testimonials_html}
                </div>
            </div>
        </section>

        <!-- Trust Badges -->
        <section class="section section-alt trust-section">
            <div class="container">
                <h2 class="section-title">{c['trust_badges']['title']}</h2>
                <div class="trust-grid">
                    {trust_badges_html}
                </div>
            </div>
        </section>

        <!-- FAQ -->
        <section class="section faq-section">
            <div class="container">
                <h2 class="section-title">{c['faq']['title']}</h2>
                <div class="faq-container">
                    {faq_html}
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="section cta-section">
            <div class="container">
                <div class="cta-content">
                    <h2>{c['cta_section']['title']}</h2>
                    <p>{c['cta_section']['subtitle']}</p>
                    <a href="{c['pages']['quote']}" class="btn btn-primary btn-lg">{c['cta_section']['button']}</a>
                </div>
            </div>
        </section>
    '''

    return get_base_template(lang, c['nav']['home'], content, 'home')


def generate_services_page(lang):
    """Generate services page content."""
    c = CONTENT[lang]
    sp = c['services_page']

    # Residential services HTML
    res_services_html = ''
    for s in sp['residential']['services']:
        res_services_html += f'''
            <div class="service-detail-card">
                <h4>{s['name']}</h4>
                <p>{s['desc']}</p>
            </div>'''

    # School services HTML
    school_services_html = ''
    for s in sp['school']['services']:
        school_services_html += f'''
            <div class="service-detail-card">
                <h4>{s['name']}</h4>
                <p>{s['desc']}</p>
            </div>'''

    content = f'''
        <!-- Page Header -->
        <section class="page-header">
            <div class="container">
                <h1>{sp['title']}</h1>
                <p>{sp['subtitle']}</p>
                <p class="green-badge">{sp['green_note']}</p>
            </div>
        </section>

        <!-- Residential Cleaning -->
        <section class="section">
            <div class="container">
                <div class="services-section">
                    <div class="services-header">
                        <h2>{sp['residential']['title']}</h2>
                        <p>{sp['residential']['intro']}</p>
                    </div>
                    <div class="services-detail-grid">
                        {res_services_html}
                    </div>
                </div>
            </div>
        </section>

        <!-- School Cleaning -->
        <section class="section section-alt">
            <div class="container">
                <div class="services-section">
                    <div class="services-header">
                        <h2>{sp['school']['title']}</h2>
                        <p>{sp['school']['intro']}</p>
                    </div>
                    <div class="services-detail-grid">
                        {school_services_html}
                    </div>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="section cta-section">
            <div class="container">
                <div class="cta-content">
                    <h2>{c['cta_section']['title']}</h2>
                    <p>{c['cta_section']['subtitle']}</p>
                    <a href="{c['pages']['quote']}" class="btn btn-primary btn-lg">{c['cta_section']['button']}</a>
                </div>
            </div>
        </section>
    '''

    return get_base_template(lang, sp['title'], content, 'services')


def generate_quote_page(lang):
    """Generate quote request page content."""
    c = CONTENT[lang]
    qp = c['quote_page']

    content = f'''
        <!-- Page Header -->
        <section class="quote-hero">
            <div class="container">
                <div class="quote-hero-content">
                    <h1>{qp['title']}</h1>
                    <p>{qp['subtitle']}</p>
                </div>
            </div>
        </section>

        <!-- Quote Form Section -->
        <section class="quote-section">
            <div class="container">
                <div class="quote-layout">
                    <!-- Form Column -->
                    <div class="quote-form-column">
                        <div class="form-container">
                            <form id="quote-form" action="{FORMSPREE_ENDPOINT}" method="POST">
                                <input type="hidden" name="_language" value="{lang}">

                                <!-- Step 1: Service Type -->
                                <div class="form-section">
                                    <div class="form-step-header">
                                        <span class="form-step-number">1</span>
                                        <h3>{qp['form']['service_type']}</h3>
                                    </div>
                                    <div class="service-type-cards">
                                        <label class="service-type-card">
                                            <input type="radio" name="service_category" value="residential" required>
                                            <div class="service-type-content">
                                                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                                                <span class="service-type-title">{qp['form']['residential_label']}</span>
                                                <span class="service-type-desc">{qp['form']['residential_desc']}</span>
                                            </div>
                                        </label>
                                        <label class="service-type-card">
                                            <input type="radio" name="service_category" value="school">
                                            <div class="service-type-content">
                                                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                                                <span class="service-type-title">{qp['form']['school_label']}</span>
                                                <span class="service-type-desc">{qp['form']['school_desc']}</span>
                                            </div>
                                        </label>
                                    </div>

                                    <div class="form-group" style="margin-top: 1.25rem;">
                                        <label for="service_detail">{qp['form']['specific_service']}</label>
                                        <input type="text" id="service_detail" name="service_detail" placeholder="{qp['form']['service_placeholder']}">
                                    </div>
                                </div>

                                <!-- Step 2: Frequency -->
                                <div class="form-section">
                                    <div class="form-step-header">
                                        <span class="form-step-number">2</span>
                                        <h3>{qp['form']['frequency']}</h3>
                                    </div>
                                    <div class="frequency-options">
                                        <label class="frequency-option">
                                            <input type="radio" name="frequency" value="one-time" required>
                                            <span class="frequency-label">{qp['form']['freq_onetime']}</span>
                                        </label>
                                        <label class="frequency-option">
                                            <input type="radio" name="frequency" value="weekly">
                                            <span class="frequency-label">{qp['form']['freq_weekly']}</span>
                                        </label>
                                        <label class="frequency-option">
                                            <input type="radio" name="frequency" value="biweekly">
                                            <span class="frequency-label">{qp['form']['freq_biweekly']}</span>
                                        </label>
                                        <label class="frequency-option">
                                            <input type="radio" name="frequency" value="monthly">
                                            <span class="frequency-label">{qp['form']['freq_monthly']}</span>
                                        </label>
                                        <label class="frequency-option">
                                            <input type="radio" name="frequency" value="custom">
                                            <span class="frequency-label">{qp['form']['freq_custom']}</span>
                                        </label>
                                    </div>
                                </div>

                                <!-- Step 3: Property Details -->
                                <div class="form-section">
                                    <div class="form-step-header">
                                        <span class="form-step-number">3</span>
                                        <h3>{qp['form']['property_details']}</h3>
                                    </div>
                                    <div class="form-row">
                                        <div class="form-group">
                                            <label for="size">{qp['form']['property_size']}</label>
                                            <input type="text" id="size" name="size" placeholder="{qp['form']['size_placeholder']}">
                                        </div>
                                        <div class="form-group">
                                            <label for="address">{qp['form']['address']}</label>
                                            <input type="text" id="address" name="address" placeholder="{qp['form']['address_placeholder']}">
                                        </div>
                                    </div>
                                </div>

                                <!-- Step 4: Contact Details -->
                                <div class="form-section">
                                    <div class="form-step-header">
                                        <span class="form-step-number">4</span>
                                        <h3>{qp['form']['contact_details']}</h3>
                                    </div>
                                    <div class="form-row">
                                        <div class="form-group">
                                            <label for="name">{qp['form']['name']}</label>
                                            <input type="text" id="name" name="name" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="phone">{qp['form']['phone']}</label>
                                            <input type="tel" id="phone" name="phone" placeholder="{qp['form']['phone_placeholder']}">
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="email">{qp['form']['email']}</label>
                                        <input type="email" id="email" name="email" required>
                                    </div>
                                </div>

                                <!-- Additional Info -->
                                <div class="form-section">
                                    <h3 class="form-section-title">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                                        {qp['form']['message']}
                                    </h3>
                                    <div class="form-group">
                                        <textarea id="message" name="message" rows="4" placeholder="{qp['form']['message_placeholder']}"></textarea>
                                    </div>
                                </div>

                                <p class="form-privacy">{qp['form']['privacy']}</p>

                                <button type="submit" class="btn btn-primary btn-lg btn-full">
                                    <span>{qp['form']['submit']}</span>
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
                                </button>
                            </form>

                            <div id="form-success" class="form-message success" style="display: none;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                                <span>{qp['success']}</span>
                            </div>

                            <div id="form-error" class="form-message error" style="display: none;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
                                <span>{qp['error']}</span>
                            </div>
                        </div>
                    </div>

                    <!-- Info Column -->
                    <div class="quote-info-column">
                        <!-- What Happens Next -->
                        <div class="quote-info-card">
                            <h3>{qp['next_steps']['title']}</h3>
                            <div class="next-steps">
                                <div class="next-step">
                                    <div class="next-step-number">1</div>
                                    <div class="next-step-content">
                                        <strong>{qp['next_steps']['step1_title']}</strong>
                                        <p>{qp['next_steps']['step1_desc']}</p>
                                    </div>
                                </div>
                                <div class="next-step">
                                    <div class="next-step-number">2</div>
                                    <div class="next-step-content">
                                        <strong>{qp['next_steps']['step2_title']}</strong>
                                        <p>{qp['next_steps']['step2_desc']}</p>
                                    </div>
                                </div>
                                <div class="next-step">
                                    <div class="next-step-number">3</div>
                                    <div class="next-step-content">
                                        <strong>{qp['next_steps']['step3_title']}</strong>
                                        <p>{qp['next_steps']['step3_desc']}</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Contact Options -->
                        <div class="quote-info-card quote-contact-card">
                            <h3>{qp['prefer_call']['title']}</h3>
                            <p>{qp['prefer_call']['desc']}</p>
                            <a href="tel:{CONTACT_INFO['phone']}" class="quote-phone-link">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                {CONTACT_INFO['phone']}
                            </a>
                            <p class="quote-hours">{CONTACT_INFO['hours'][lang]}</p>
                        </div>

                        <!-- Trust Indicators -->
                        <div class="quote-trust-badges">
                            <div class="quote-trust-item">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                                <span>{qp['trust']['free']}</span>
                            </div>
                            <div class="quote-trust-item">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                                <span>{qp['trust']['response']}</span>
                            </div>
                            <div class="quote-trust-item">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                                <span>{qp['trust']['obligation']}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    '''

    return get_base_template(lang, qp['title'], content, 'quote')


def generate_about_page(lang):
    """Generate about page content."""
    c = CONTENT[lang]
    ap = c['about_page']

    # Story paragraphs HTML
    story_html = ''
    for p in ap['story']['paragraphs']:
        story_html += f'<p>{p}</p>'

    # Values HTML
    values_html = ''
    for v in ap['values']['items']:
        values_html += f'''
            <div class="value-card">
                <h3>{v['title']}</h3>
                <p>{v['desc']}</p>
            </div>'''

    # Service areas HTML
    areas_html = ''
    for area in ap['service_area']['areas']:
        areas_html += f'<li>{area}</li>'

    content = f'''
        <!-- Page Header -->
        <section class="page-header">
            <div class="container">
                <h1>{ap['title']}</h1>
                <p>{ap['subtitle']}</p>
            </div>
        </section>

        <!-- Our Story -->
        <section class="section">
            <div class="container">
                <div class="about-story">
                    <h2>{ap['story']['title']}</h2>
                    {story_html}
                </div>
            </div>
        </section>

        <!-- Our Values -->
        <section class="section section-alt">
            <div class="container">
                <h2 class="section-title">{ap['values']['title']}</h2>
                <div class="values-grid">
                    {values_html}
                </div>
            </div>
        </section>

        <!-- Service Area -->
        <section class="section">
            <div class="container">
                <div class="service-area">
                    <h2>{ap['service_area']['title']}</h2>
                    <p>{ap['service_area']['desc']}</p>
                    <ul class="areas-list">
                        {areas_html}
                    </ul>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="section cta-section">
            <div class="container">
                <div class="cta-content">
                    <h2>{c['cta_section']['title']}</h2>
                    <p>{c['cta_section']['subtitle']}</p>
                    <a href="{c['pages']['quote']}" class="btn btn-primary btn-lg">{c['cta_section']['button']}</a>
                </div>
            </div>
        </section>
    '''

    return get_base_template(lang, ap['title'], content, 'about')


def generate_landing_page():
    """Generate the language detection landing page."""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Lidice's Cleaning Services - Eco-friendly professional cleaning in Stockholm. 100% green products.">
    <title>Lidice's Cleaning Services | Stockholm</title>

    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        }

        .landing-container {
            text-align: center;
            padding: 3rem 2rem;
            max-width: 500px;
        }

        h1 {
            font-size: 1.75rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 0.5rem;
        }

        .tagline {
            color: #6b7280;
            margin-bottom: 0.75rem;
            font-size: 1rem;
        }

        .green-note {
            color: #15803d;
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 2.5rem;
        }

        .lang-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .lang-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1rem 2.5rem;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.2s ease;
            min-width: 140px;
        }

        .lang-btn-en {
            background: #16a34a;
            color: white;
        }

        .lang-btn-en:hover {
            background: #15803d;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(22, 163, 74, 0.3);
        }

        .lang-btn-sv {
            background: white;
            color: #1f2937;
            border: 2px solid #e5e7eb;
        }

        .lang-btn-sv:hover {
            border-color: #16a34a;
            color: #16a34a;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="landing-container">
        <h1>Lidice's Cleaning Services</h1>
        <p class="tagline">Professional Cleaning in Stockholm</p>
        <p class="green-note">100% Eco-Friendly Products</p>

        <div class="lang-buttons">
            <a href="en/index.html" class="lang-btn lang-btn-en">English</a>
            <a href="sv/index.html" class="lang-btn lang-btn-sv">Svenska</a>
        </div>
    </div>

    <script>
        (function() {
            var savedLang = localStorage.getItem('lidice-lang');
            if (savedLang) {
                window.location.href = savedLang + '/index.html';
            }
        })();
    </script>
</body>
</html>'''


# =============================================================================
# CSS STYLES
# =============================================================================

def get_css():
    """Generate CSS stylesheet."""
    return '''/* =============================================================================
   Lidice's Cleaning Services - Stylesheet
   Professional, Clean Design with Green/Eco Focus
   ============================================================================= */

/* CSS Variables */
:root {
    --primary: #16a34a;
    --primary-dark: #15803d;
    --primary-light: #22c55e;
    --text: #1f2937;
    --text-light: #6b7280;
    --text-lighter: #9ca3af;
    --bg: #ffffff;
    --bg-alt: #f9fafb;
    --bg-green: #f0fdf4;
    --border: #e5e7eb;
    --shadow: rgba(0, 0, 0, 0.1);
    --shadow-lg: rgba(0, 0, 0, 0.15);
    --radius: 8px;
    --radius-lg: 12px;
    --transition: 0.2s ease;
}

/* Reset & Base */
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: var(--text);
    background: var(--bg);
}

img {
    max-width: 100%;
    height: auto;
}

a {
    color: var(--primary);
    text-decoration: none;
    transition: color var(--transition);
}

a:hover {
    color: var(--primary-dark);
}

/* Container */
.container {
    width: 100%;
    max-width: 1140px;
    margin: 0 auto;
    padding: 0 1.5rem;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    line-height: 1.2;
    color: var(--text);
}

h1 { font-size: 2.5rem; }
h2 { font-size: 1.875rem; }
h3 { font-size: 1.25rem; }
h4 { font-size: 1.125rem; }

@media (max-width: 768px) {
    h1 { font-size: 2rem; }
    h2 { font-size: 1.5rem; }
}

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    border: none;
    border-radius: var(--radius);
    cursor: pointer;
    transition: all var(--transition);
}

.btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
}

.btn-lg {
    padding: 1rem 2rem;
    font-size: 1.0625rem;
}

.btn-full {
    width: 100%;
}

.btn-primary {
    background: var(--primary);
    color: white;
}

.btn-primary:hover {
    background: var(--primary-dark);
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(22, 163, 74, 0.3);
}

/* =============================================================================
   Header & Navigation
   ============================================================================= */

.header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
}

.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 70px;
}

.logo {
    display: flex;
    align-items: center;
    font-weight: 700;
    font-size: 1.25rem;
    color: var(--text);
}

.logo:hover {
    color: var(--text);
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-links a {
    font-weight: 500;
    color: var(--text-light);
    padding: 0.5rem 0;
    position: relative;
}

.nav-links a:hover,
.nav-links a.active {
    color: var(--primary);
}

.nav-links a.active::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--primary);
}

.nav-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.lang-switch {
    font-size: 0.875rem;
    font-weight: 600;
    padding: 0.375rem 0.75rem;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text-light);
    transition: all var(--transition);
}

.lang-switch:hover {
    border-color: var(--primary);
    color: var(--primary);
}

/* Mobile Menu Button */
.mobile-menu-btn {
    display: none;
    flex-direction: column;
    justify-content: center;
    gap: 5px;
    width: 28px;
    height: 28px;
    background: none;
    border: none;
    cursor: pointer;
}

.mobile-menu-btn span {
    display: block;
    width: 100%;
    height: 2px;
    background: var(--text);
    border-radius: 2px;
    transition: all var(--transition);
}

/* Mobile Menu */
.mobile-menu {
    display: none;
    position: fixed;
    top: 70px;
    left: 0;
    right: 0;
    background: white;
    border-bottom: 1px solid var(--border);
    padding: 1rem;
    z-index: 999;
}

.mobile-menu.active {
    display: block;
}

.mobile-nav-links {
    list-style: none;
}

.mobile-nav-links li {
    border-bottom: 1px solid var(--border);
}

.mobile-nav-links li:last-child {
    border-bottom: none;
}

.mobile-nav-links a {
    display: block;
    padding: 1rem;
    color: var(--text);
    font-weight: 500;
}

@media (max-width: 768px) {
    .nav-links,
    .nav-actions .btn {
        display: none;
    }

    .mobile-menu-btn {
        display: flex;
    }
}

/* =============================================================================
   Sections
   ============================================================================= */

.section {
    padding: 5rem 0;
}

.section-alt {
    background: var(--bg-alt);
}

.section-green {
    background: var(--bg-green);
}

.section-title {
    text-align: center;
    margin-bottom: 1rem;
}

.section-subtitle {
    text-align: center;
    color: var(--text-light);
    margin-bottom: 2.5rem;
}

.page-header {
    padding: 8rem 0 4rem;
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    text-align: center;
}

.page-header h1 {
    margin-bottom: 0.5rem;
}

.page-header p {
    color: var(--text-light);
    font-size: 1.0625rem;
}

.green-badge {
    display: inline-block;
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    background: var(--primary);
    color: white;
    font-size: 0.875rem;
    font-weight: 500;
    border-radius: 20px;
}

/* =============================================================================
   Hero Section
   ============================================================================= */

.hero {
    padding: 10rem 0 6rem;
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    overflow: hidden;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

.hero-content {
    max-width: 600px;
}

.hero-illustration {
    display: flex;
    justify-content: center;
}

.hero-illustration svg {
    width: 100%;
    max-width: 400px;
    height: auto;
}

.hero h1 {
    font-size: 2.75rem;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-light);
    margin-bottom: 2rem;
}

@media (max-width: 992px) {
    .hero-grid {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .hero-content {
        max-width: 600px;
        margin: 0 auto;
    }

    .hero-illustration {
        order: -1;
        margin-bottom: 2rem;
    }

    .hero-illustration svg {
        max-width: 300px;
    }
}

@media (max-width: 768px) {
    .hero {
        padding: 8rem 0 4rem;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .hero-subtitle {
        font-size: 1rem;
    }

    .hero-illustration svg {
        max-width: 250px;
    }
}

.hero-actions {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

.hero-phone {
    font-size: 0.9375rem;
    color: var(--text-light);
}

.hero-phone a {
    font-weight: 600;
    color: var(--primary);
}

.hero-phone a:hover {
    color: var(--primary-dark);
}

/* =============================================================================
   Stats Bar
   ============================================================================= */

.stats-bar {
    background: var(--text);
    padding: 2rem 0;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
}

.stat-item {
    text-align: center;
    color: white;
}

.stat-number {
    display: block;
    font-size: 2.25rem;
    font-weight: 700;
    color: var(--primary-light);
    line-height: 1.2;
}

.stat-label {
    display: block;
    font-size: 0.875rem;
    color: var(--text-lighter);
    margin-top: 0.25rem;
}

@media (max-width: 768px) {
    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }

    .stat-number {
        font-size: 1.75rem;
    }
}

/* =============================================================================
   How It Works
   ============================================================================= */

.how-it-works {
    background: var(--bg-alt);
}

.steps-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    max-width: 900px;
    margin: 0 auto;
}

.step-card {
    text-align: center;
    padding: 2rem 1.5rem;
    background: white;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
}

.step-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    background: var(--primary);
    color: white;
    font-size: 1.25rem;
    font-weight: 700;
    border-radius: 50%;
    margin-bottom: 1rem;
}

.step-card h3 {
    margin-bottom: 0.75rem;
    font-size: 1.125rem;
}

.step-card p {
    color: var(--text-light);
    font-size: 0.9375rem;
    line-height: 1.6;
}

@media (max-width: 768px) {
    .steps-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }

    .step-card {
        padding: 1.5rem;
    }
}

/* =============================================================================
   Services Overview
   ============================================================================= */

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
}

.service-card {
    display: block;
    background: white;
    padding: 2rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    transition: all var(--transition);
    color: var(--text);
}

.service-card:hover {
    border-color: var(--primary);
    box-shadow: 0 8px 30px var(--shadow);
    color: var(--text);
}

.service-card h3 {
    margin-bottom: 0.75rem;
}

.service-card p {
    color: var(--text-light);
    margin-bottom: 1rem;
}

.card-link {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--primary);
}

/* =============================================================================
   Green Commitment Section
   ============================================================================= */

.green-section {
    text-align: center;
}

.green-intro {
    max-width: 700px;
    margin: 0 auto 3rem;
    color: var(--text-light);
    font-size: 1.0625rem;
}

.green-points-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    text-align: left;
}

.green-point {
    background: white;
    padding: 1.5rem;
    border-radius: var(--radius);
    border-left: 4px solid var(--primary);
}

.green-point h3 {
    margin-bottom: 0.5rem;
    font-size: 1.0625rem;
}

.green-point p {
    color: var(--text-light);
    font-size: 0.9375rem;
}

/* =============================================================================
   Testimonials
   ============================================================================= */

.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
}

.testimonial-card {
    background: white;
    padding: 1.75rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
}

.testimonial-text {
    font-size: 1rem;
    color: var(--text);
    margin-bottom: 1.25rem;
    line-height: 1.7;
}

.testimonial-author {
    display: flex;
    flex-direction: column;
    gap: 0.125rem;
}

.testimonial-author strong {
    color: var(--text);
    font-size: 0.9375rem;
}

.testimonial-role {
    color: var(--primary);
    font-size: 0.8125rem;
    font-weight: 500;
}

.testimonial-location {
    color: var(--text-light);
    font-size: 0.8125rem;
}

/* =============================================================================
   Trust Badges
   ============================================================================= */

.trust-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
}

.trust-badge {
    text-align: center;
    padding: 1.5rem 1rem;
}

.trust-badge h3 {
    font-size: 1rem;
    margin-bottom: 0.5rem;
    color: var(--text);
}

.trust-badge p {
    font-size: 0.875rem;
    color: var(--text-light);
    line-height: 1.5;
}

@media (max-width: 992px) {
    .trust-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 576px) {
    .trust-grid {
        grid-template-columns: 1fr;
    }
}

/* =============================================================================
   FAQ Section
   ============================================================================= */

.faq-container {
    max-width: 800px;
    margin: 0 auto;
}

.faq-item {
    border-bottom: 1px solid var(--border);
}

.faq-item:last-child {
    border-bottom: none;
}

.faq-question {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.25rem 0;
    background: none;
    border: none;
    cursor: pointer;
    text-align: left;
    font-family: inherit;
    font-size: 1rem;
    font-weight: 600;
    color: var(--text);
    transition: color var(--transition);
}

.faq-question:hover {
    color: var(--primary);
}

.faq-question span:first-child {
    flex: 1;
    padding-right: 1rem;
}

.faq-icon {
    font-size: 1.5rem;
    font-weight: 300;
    color: var(--primary);
    transition: transform var(--transition);
}

.faq-item.active .faq-icon {
    transform: rotate(45deg);
}

.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease, padding 0.3s ease;
}

.faq-item.active .faq-answer {
    max-height: 300px;
    padding-bottom: 1.25rem;
}

.faq-answer p {
    color: var(--text-light);
    line-height: 1.7;
}

/* =============================================================================
   CTA Section
   ============================================================================= */

.cta-section {
    background: var(--primary);
    color: white;
}

.cta-content {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
}

.cta-content h2 {
    color: white;
    margin-bottom: 0.75rem;
}

.cta-content p {
    opacity: 0.9;
    margin-bottom: 2rem;
}

.cta-section .btn-primary {
    background: white;
    color: var(--primary);
}

.cta-section .btn-primary:hover {
    background: #f0fdf4;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

/* =============================================================================
   Services Page
   ============================================================================= */

.services-section {
    max-width: 900px;
    margin: 0 auto;
}

.services-header {
    margin-bottom: 2rem;
}

.services-header h2 {
    margin-bottom: 0.75rem;
}

.services-header p {
    color: var(--text-light);
}

.services-detail-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.25rem;
}

.service-detail-card {
    background: white;
    padding: 1.5rem;
    border-radius: var(--radius);
    border: 1px solid var(--border);
    transition: all var(--transition);
}

.section-alt .service-detail-card {
    background: var(--bg);
}

.service-detail-card:hover {
    border-color: var(--primary);
}

.service-detail-card h4 {
    margin-bottom: 0.5rem;
    color: var(--text);
}

.service-detail-card p {
    color: var(--text-light);
    font-size: 0.9375rem;
}

/* =============================================================================
   Quote Page - Redesigned
   ============================================================================= */

.quote-hero {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    padding: 8rem 0 4rem;
    text-align: center;
}

.quote-hero h1 {
    font-size: 2.5rem;
    color: var(--text);
    margin-bottom: 0.75rem;
}

.quote-hero p {
    color: var(--text-light);
    font-size: 1.125rem;
}

.quote-section {
    padding: 4rem 0;
    background: var(--bg-alt);
}

.quote-layout {
    display: grid;
    grid-template-columns: 1fr 380px;
    gap: 3rem;
    align-items: start;
}

.quote-form-column .form-container {
    background: white;
    padding: 2rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.form-section {
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border);
}

.form-section:last-of-type {
    border-bottom: none;
    padding-bottom: 0;
    margin-bottom: 1.5rem;
}

.form-section-title {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1rem;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 1.25rem;
}

.form-section-title svg {
    color: var(--primary);
}

/* Step-based form headers */
.form-step-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.25rem;
}

.form-step-header h3 {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text);
    margin: 0;
}

.form-step-number {
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--primary);
    color: white;
    border-radius: 50%;
    font-size: 0.875rem;
    font-weight: 600;
    flex-shrink: 0;
}

/* Service Type Cards */
.service-type-cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}

.service-type-card {
    cursor: pointer;
}

.service-type-card input {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}

.service-type-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 1.5rem 1rem;
    border: 2px solid var(--border);
    border-radius: var(--radius);
    background: white;
    transition: all var(--transition);
}

.service-type-card:hover .service-type-content {
    border-color: var(--primary);
    background: rgba(22, 163, 74, 0.02);
}

.service-type-card input:checked + .service-type-content {
    border-color: var(--primary);
    background: rgba(22, 163, 74, 0.05);
    box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.15);
}

.service-type-content svg {
    color: var(--primary);
    margin-bottom: 0.75rem;
}

.service-type-title {
    font-weight: 600;
    color: var(--text);
    font-size: 1rem;
    margin-bottom: 0.25rem;
}

.service-type-desc {
    font-size: 0.8125rem;
    color: var(--text-light);
}

/* Frequency Options */
.frequency-options {
    display: flex;
    flex-wrap: wrap;
    gap: 0.625rem;
}

.frequency-option {
    cursor: pointer;
}

.frequency-option input {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}

.frequency-label {
    display: inline-block;
    padding: 0.625rem 1.125rem;
    border: 1px solid var(--border);
    border-radius: 100px;
    background: white;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text);
    transition: all var(--transition);
}

.frequency-option:hover .frequency-label {
    border-color: var(--primary);
    color: var(--primary);
}

.frequency-option input:checked + .frequency-label {
    background: var(--primary);
    border-color: var(--primary);
    color: white;
}

.form-row {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}

.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    font-weight: 500;
    margin-bottom: 0.375rem;
    color: var(--text);
    font-size: 0.875rem;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    font-size: 0.9375rem;
    font-family: inherit;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    background: white;
    transition: border-color var(--transition), box-shadow var(--transition);
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1);
}

.form-group input::placeholder,
.form-group textarea::placeholder {
    color: #9ca3af;
}

.form-group textarea {
    resize: vertical;
    min-height: 100px;
}

.form-privacy {
    font-size: 0.8125rem;
    color: var(--text-light);
    margin-bottom: 1.25rem;
}

.btn-full {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.btn-full svg {
    transition: transform var(--transition);
}

.btn-full:hover svg {
    transform: translateX(4px);
}

.form-message {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    padding: 1.25rem;
    border-radius: var(--radius);
    margin-top: 1.25rem;
    font-weight: 500;
}

.form-message.success {
    background: #d1fae5;
    color: #065f46;
}

.form-message.error {
    background: #fee2e2;
    color: #991b1b;
}

/* Quote Info Column */
.quote-info-column {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.quote-info-card {
    background: white;
    padding: 1.5rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
}

.quote-info-card h3 {
    font-size: 1rem;
    margin-bottom: 1rem;
    color: var(--text);
}

.next-steps {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.next-step {
    display: flex;
    gap: 1rem;
    align-items: flex-start;
}

.next-step-number {
    width: 28px;
    height: 28px;
    background: var(--primary);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8125rem;
    font-weight: 600;
    flex-shrink: 0;
}

.next-step-content strong {
    display: block;
    font-size: 0.9375rem;
    margin-bottom: 0.25rem;
}

.next-step-content p {
    font-size: 0.8125rem;
    color: var(--text-light);
    line-height: 1.5;
}

.quote-contact-card {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    text-align: center;
}

.quote-contact-card h3 {
    color: var(--primary-dark);
}

.quote-contact-card > p {
    font-size: 0.875rem;
    color: var(--text-light);
    margin-bottom: 1rem;
}

.quote-phone-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--primary);
    margin-bottom: 0.5rem;
}

.quote-phone-link:hover {
    color: var(--primary-dark);
}

.quote-hours {
    font-size: 0.8125rem;
    color: var(--text-light);
}

.quote-trust-badges {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    background: white;
    padding: 1.25rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
}

.quote-trust-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.875rem;
    color: var(--text);
}

.quote-trust-item svg {
    color: var(--primary);
    flex-shrink: 0;
}

@media (max-width: 992px) {
    .quote-layout {
        grid-template-columns: 1fr;
    }

    .quote-info-column {
        order: -1;
        flex-direction: row;
        flex-wrap: wrap;
    }

    .quote-info-card {
        flex: 1;
        min-width: 280px;
    }

    .quote-trust-badges {
        flex-direction: row;
        justify-content: center;
        width: 100%;
    }
}

@media (max-width: 768px) {
    .quote-hero {
        padding: 6rem 0 3rem;
    }

    .quote-hero h1 {
        font-size: 1.75rem;
    }

    .quote-section {
        padding: 2rem 0;
    }

    .quote-form-column .form-container {
        padding: 1.5rem;
    }

    .form-row {
        grid-template-columns: 1fr;
    }

    .service-type-cards {
        grid-template-columns: 1fr;
    }

    .frequency-options {
        gap: 0.5rem;
    }

    .frequency-label {
        padding: 0.5rem 0.875rem;
        font-size: 0.8125rem;
    }

    .quote-info-column {
        flex-direction: column;
    }

    .quote-trust-badges {
        flex-direction: column;
    }
}

/* Contact Cards - Legacy */
.contact-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1.5rem;
    max-width: 700px;
    margin: 0 auto;
}

.contact-card {
    text-align: center;
    padding: 1.5rem;
    background: white;
    border-radius: var(--radius);
    border: 1px solid var(--border);
}

.contact-card h3 {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-light);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.5rem;
}

.contact-card a,
.contact-card p {
    color: var(--text);
    font-weight: 500;
}

.contact-card a:hover {
    color: var(--primary);
}

/* =============================================================================
   About Page
   ============================================================================= */

.about-story {
    max-width: 700px;
    margin: 0 auto;
}

.about-story h2 {
    margin-bottom: 1.5rem;
}

.about-story p {
    color: var(--text-light);
    margin-bottom: 1rem;
    line-height: 1.8;
}

.values-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
}

.value-card {
    padding: 1.5rem;
    background: white;
    border-radius: var(--radius);
    border: 1px solid var(--border);
}

.value-card h3 {
    margin-bottom: 0.5rem;
    font-size: 1.0625rem;
}

.value-card p {
    color: var(--text-light);
    font-size: 0.9375rem;
}

.service-area {
    text-align: center;
    max-width: 700px;
    margin: 0 auto;
}

.service-area h2 {
    margin-bottom: 0.75rem;
}

.service-area > p {
    color: var(--text-light);
    margin-bottom: 1.5rem;
}

.areas-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    list-style: none;
}

.areas-list li {
    background: var(--bg-alt);
    padding: 0.375rem 0.875rem;
    border-radius: 20px;
    font-size: 0.875rem;
    color: var(--text-light);
}

/* =============================================================================
   Footer
   ============================================================================= */

.footer {
    background: var(--text);
    color: white;
    padding: 4rem 0 2rem;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 2rem;
    margin-bottom: 2.5rem;
}

.footer-brand .logo {
    color: white;
    margin-bottom: 0.5rem;
}

.footer-brand p {
    color: var(--text-lighter);
    font-size: 0.875rem;
}

.footer h4 {
    color: white;
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.75rem;
}

.footer ul {
    list-style: none;
}

.footer ul li {
    margin-bottom: 0.375rem;
}

.footer ul a,
.footer ul li,
.footer p:not(.footer-brand p) {
    color: var(--text-lighter);
    font-size: 0.875rem;
}

.footer ul a:hover {
    color: white;
}

.footer-bottom {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-bottom p {
    color: var(--text-lighter);
    font-size: 0.8125rem;
}

@media (max-width: 768px) {
    .footer {
        padding: 3rem 0 1.5rem;
    }

    .footer-grid {
        text-align: center;
    }
}

/* =============================================================================
   Back to Top Button
   ============================================================================= */

.back-to-top {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    width: 48px;
    height: 48px;
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    visibility: hidden;
    transition: all var(--transition);
    box-shadow: 0 4px 12px rgba(22, 163, 74, 0.3);
    z-index: 100;
}

.back-to-top:hover {
    background: var(--primary-dark);
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(22, 163, 74, 0.4);
}

.back-to-top.visible {
    opacity: 1;
    visibility: visible;
}

@media (max-width: 768px) {
    .back-to-top {
        bottom: 1.5rem;
        right: 1.5rem;
        width: 44px;
        height: 44px;
    }
}

/* =============================================================================
   Social Links
   ============================================================================= */

.social-links {
    display: flex;
    gap: 0.75rem;
}

.social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    color: var(--text-lighter);
    transition: all var(--transition);
}

.social-link:hover {
    background: var(--primary);
    color: white;
    transform: translateY(-2px);
}

.social-link svg {
    width: 18px;
    height: 18px;
}

/* =============================================================================
   Cookie Consent Banner
   ============================================================================= */

.cookie-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: var(--text);
    color: white;
    padding: 1rem 0;
    z-index: 1000;
    transform: translateY(100%);
    transition: transform 0.3s ease;
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.15);
}

.cookie-banner.visible {
    transform: translateY(0);
}

.cookie-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
}

.cookie-content p {
    font-size: 0.9375rem;
    color: var(--text-lighter);
    margin: 0;
}

.cookie-actions {
    display: flex;
    gap: 0.75rem;
    flex-shrink: 0;
}

.cookie-btn {
    padding: 0.625rem 1.25rem;
    font-size: 0.875rem;
    font-weight: 500;
    border-radius: var(--radius);
    cursor: pointer;
    transition: all var(--transition);
    border: none;
    font-family: inherit;
}

.cookie-accept {
    background: var(--primary);
    color: white;
}

.cookie-accept:hover {
    background: var(--primary-dark);
}

.cookie-decline {
    background: transparent;
    color: var(--text-lighter);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.cookie-decline:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
}

@media (max-width: 768px) {
    .cookie-content {
        flex-direction: column;
        text-align: center;
        padding: 0 1rem;
    }

    .cookie-content p {
        font-size: 0.875rem;
    }

    .cookie-actions {
        width: 100%;
        justify-content: center;
    }
}
'''


# =============================================================================
# JAVASCRIPT
# =============================================================================

def get_js():
    """Generate JavaScript file."""
    return '''// Lidice's Cleaning Services - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    var mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    var mobileMenu = document.querySelector('.mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');

            var spans = mobileMenuBtn.querySelectorAll('span');
            if (mobileMenu.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
            } else {
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
            }
        });

        mobileMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
            });
        });
    }

    // Save language preference
    var langSwitch = document.querySelector('.lang-switch');
    if (langSwitch) {
        langSwitch.addEventListener('click', function() {
            var href = this.getAttribute('href');
            var lang = href.includes('/sv/') ? 'sv' : 'en';
            localStorage.setItem('lidice-lang', lang);
        });
    }

    var htmlLang = document.documentElement.lang;
    if (htmlLang === 'en' || htmlLang === 'sv') {
        localStorage.setItem('lidice-lang', htmlLang);
    }

    // Quote Form Handling
    var quoteForm = document.getElementById('quote-form');
    var successMessage = document.getElementById('form-success');
    var errorMessage = document.getElementById('form-error');

    if (quoteForm) {
        quoteForm.addEventListener('submit', function(e) {
            e.preventDefault();

            var submitBtn = quoteForm.querySelector('button[type="submit"]');
            var originalText = submitBtn.textContent;
            submitBtn.textContent = '...';
            submitBtn.disabled = true;

            if (successMessage) successMessage.style.display = 'none';
            if (errorMessage) errorMessage.style.display = 'none';

            var formData = new FormData(quoteForm);

            fetch(quoteForm.action, {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            })
            .then(function(response) {
                if (response.ok) {
                    quoteForm.reset();
                    if (successMessage) successMessage.style.display = 'block';
                    quoteForm.style.display = 'none';
                } else {
                    throw new Error('Form submission failed');
                }
            })
            .catch(function(error) {
                console.error('Error:', error);
                if (errorMessage) errorMessage.style.display = 'block';
            })
            .finally(function() {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            });
        });
    }

    // Header scroll effect
    var header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.08)';
            } else {
                header.style.boxShadow = '';
            }
        });
    }

    // FAQ Accordion
    var faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(function(question) {
        question.addEventListener('click', function() {
            var faqItem = this.parentElement;
            var isActive = faqItem.classList.contains('active');

            // Close all FAQ items
            document.querySelectorAll('.faq-item').forEach(function(item) {
                item.classList.remove('active');
                item.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            });

            // Open clicked item if it was not active
            if (!isActive) {
                faqItem.classList.add('active');
                this.setAttribute('aria-expanded', 'true');
            }
        });
    });

    // Back to Top Button
    var backToTop = document.querySelector('.back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Cookie Consent Banner
    var cookieBanner = document.getElementById('cookie-banner');
    var cookieAccept = document.getElementById('cookie-accept');
    var cookieDecline = document.getElementById('cookie-decline');

    if (cookieBanner) {
        var cookieConsent = localStorage.getItem('lidice-cookie-consent');

        if (!cookieConsent) {
            setTimeout(function() {
                cookieBanner.classList.add('visible');
            }, 1000);
        }

        if (cookieAccept) {
            cookieAccept.addEventListener('click', function() {
                localStorage.setItem('lidice-cookie-consent', 'accepted');
                cookieBanner.classList.remove('visible');
            });
        }

        if (cookieDecline) {
            cookieDecline.addEventListener('click', function() {
                localStorage.setItem('lidice-cookie-consent', 'declined');
                cookieBanner.classList.remove('visible');
            });
        }
    }
});
'''


# =============================================================================
# MAIN GENERATOR
# =============================================================================

def main():
    """Generate the complete static website."""
    print("Generating Lidice's Cleaning Services website...")

    # Clean output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    # Create directory structure
    dirs = [
        OUTPUT_DIR,
        OUTPUT_DIR / 'en',
        OUTPUT_DIR / 'sv',
        OUTPUT_DIR / 'css',
        OUTPUT_DIR / 'js',
        OUTPUT_DIR / 'images'
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  Created {d}")

    # Generate landing page
    (OUTPUT_DIR / 'index.html').write_text(generate_landing_page(), encoding='utf-8')
    print("  Generated landing page")

    # Generate English pages
    (OUTPUT_DIR / 'en' / 'index.html').write_text(generate_home_page('en'), encoding='utf-8')
    (OUTPUT_DIR / 'en' / 'services.html').write_text(generate_services_page('en'), encoding='utf-8')
    (OUTPUT_DIR / 'en' / 'quote.html').write_text(generate_quote_page('en'), encoding='utf-8')
    (OUTPUT_DIR / 'en' / 'about.html').write_text(generate_about_page('en'), encoding='utf-8')
    print("  Generated English pages")

    # Generate Swedish pages
    (OUTPUT_DIR / 'sv' / 'index.html').write_text(generate_home_page('sv'), encoding='utf-8')
    (OUTPUT_DIR / 'sv' / 'tjanster.html').write_text(generate_services_page('sv'), encoding='utf-8')
    (OUTPUT_DIR / 'sv' / 'offert.html').write_text(generate_quote_page('sv'), encoding='utf-8')
    (OUTPUT_DIR / 'sv' / 'om-oss.html').write_text(generate_about_page('sv'), encoding='utf-8')
    print("  Generated Swedish pages")

    # Generate CSS
    (OUTPUT_DIR / 'css' / 'style.css').write_text(get_css(), encoding='utf-8')
    print("  Generated stylesheet")

    # Generate JavaScript
    (OUTPUT_DIR / 'js' / 'main.js').write_text(get_js(), encoding='utf-8')
    print("  Generated JavaScript")

    # Create placeholder for images
    (OUTPUT_DIR / 'images' / '.gitkeep').write_text('', encoding='utf-8')

    # Generate favicon (leaf icon)
    favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <circle cx="16" cy="16" r="16" fill="#16a34a"/>
  <path d="M16 6c-5.5 0-10 4.5-10 10 0 4.5 3 8.3 7 9.5 0-2.5.5-5 2-7-1.5 1-3 3-3 5.5.5.2 1 .3 1.5.4 0-3.5 2.5-6.5 5.5-8-.5 2-1 4.5-1 7 0 .5 0 1 .1 1.5h1.8c.1-.5.1-1 .1-1.5 0-2.5-.5-5-1-7 3 1.5 5.5 4.5 5.5 8 .5-.1 1-.2 1.5-.4 0-2.5-1.5-4.5-3-5.5 1.5 2 2 4.5 2 7 4-1.2 7-5 7-9.5 0-5.5-4.5-10-10-10z" fill="white"/>
</svg>'''
    (OUTPUT_DIR / 'images' / 'favicon.svg').write_text(favicon_svg, encoding='utf-8')
    print("  Generated favicon")

    # Generate sitemap.xml
    base_url = "https://cubreto.github.io/lidice-cleaning"
    today = datetime.now().strftime('%Y-%m-%d')
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{base_url}/</loc>
        <lastmod>{today}</lastmod>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{base_url}/en/index.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{base_url}/en/services.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{base_url}/en/quote.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{base_url}/en/about.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{base_url}/sv/index.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{base_url}/sv/tjanster.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{base_url}/sv/offert.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{base_url}/sv/om-oss.html</loc>
        <lastmod>{today}</lastmod>
        <priority>0.7</priority>
    </url>
</urlset>'''
    (OUTPUT_DIR / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    print("  Generated sitemap.xml")

    # Generate robots.txt
    robots = f'''User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
'''
    (OUTPUT_DIR / 'robots.txt').write_text(robots, encoding='utf-8')
    print("  Generated robots.txt")

    print("\nWebsite generated successfully.")
    print(f"\nOutput directory: {OUTPUT_DIR.absolute()}")
    print("\nTo view locally:")
    print(f"  cd {OUTPUT_DIR} && python3 -m http.server 8000")
    print("  Then open http://localhost:8000")


if __name__ == '__main__':
    main()
