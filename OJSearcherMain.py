'''
Created on Nov 29, 2011

@author: John
'''

def main():

    
    return

def build_data_mapping():
    import OJSearcher
    service_type_list = ['auto','bars and restaurants','beauty','churches','computers','diet and health','electronics','entertainment','finance','fitness','home','insurance','legal','lessons and training','markets','medical','movers and storage','office products and supplies','pets and animals','professional services','real estate','recreation and sports']
    service_type_list.append('schools')
    service_type_list.append('shopping')
    service_type_list.append('transportation')
    service_type_list.append('travel')
    cat_name_list = get_cat_data()
    searcherInst = OJSearcher.Searcher
    searcherInst.create_tables()
    searcherInst.insert_mapping_data(cat_name_list, service_type_list)
    return

def get_cat_data():
    mlist =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    #mlist.append("auto")
    mlist[0].append("Auto Body")
    mlist[0].append("Auto Dealers")
    mlist[0].append("Auto Glass")
    mlist[0].append("Auto Parts")
    mlist[0].append("Auto Repair")
    mlist[0].append("Auto Wrecking")
    mlist[0].append("Brake Repair")
    mlist[0].append("Car Alarms")
    mlist[0].append("Car Appraisals")
    mlist[0].append("Car Stereo")
    mlist[0].append("Car Washes")
    mlist[0].append("Engine Parts")
    mlist[0].append("Gas Stations")
    mlist[0].append("Motorcycle Accessories")
    mlist[0].append("Motorcycle Dealers")
    mlist[0].append("Motorcycle Parts")
    mlist[0].append("Motorcycle Repair")
    mlist[0].append("Motorhomes")
    mlist[0].append("Oil Change")
    mlist[0].append("Tires")
    mlist[0].append("Towing")
    mlist[0].append("Trailer Rental")
    mlist[0].append("Trailers")
    mlist[0].append("Truck Dealers")
    mlist[0].append("Truck Parts")
    mlist[0].append("Truck Rental")
    mlist[0].append("Truck Repair")
    mlist[0].append("Wheels & Rims")
    
    #mlist.append("Bars & Restaurants")
    mlist[1].append("Ale Houses")
    mlist[1].append("Bars")
    mlist[1].append("Cafes")
    mlist[1].append("Chinese Restaurants")
    mlist[1].append("Cocktail Lounges")
    mlist[1].append("Coffee Shops")
    mlist[1].append("Family Restaurants")
    mlist[1].append("Fast food")
    mlist[1].append("French Restaurants")
    mlist[1].append("Indian Restaurants")
    mlist[1].append("Internet Cafes")
    mlist[1].append("Italian Restaurants")
    mlist[1].append("Japanese Restaurants")
    mlist[1].append("Mexican Restaurants")
    mlist[1].append("Pizza")
    mlist[1].append("Pubs")
    mlist[1].append("Lounges")    
    mlist[1].append("Seafood Restaurants")
    mlist[1].append("Sports Bars")
    mlist[1].append("Steak Restaurants")
    mlist[1].append("Sushi")
    mlist[1].append("Take Out Restaurants")
    mlist[1].append("Taverns")
    mlist[1].append("Tea Houses")
    mlist[1].append("Thai Restaurants")
    mlist[1].append("Vegetarian Restaurants")
    mlist[1].append("Wine Bars")
    mlist[1].append("Wineries")
    
    #mlist.append("Beauty")
    mlist[2].append("Barbers")
    mlist[2].append("Beauty Consultants")
    mlist[2].append("Beauty Supplies")
    mlist[2].append("Body Piercing")
    mlist[2].append("Cosmetology")
    mlist[2].append("Day Spas")
    mlist[2].append("Electrolysis")
    mlist[2].append("Facials")
    mlist[2].append("Hair Removal")
    mlist[2].append("Hair Restoration")
    mlist[2].append("Hair Salons")
    mlist[2].append("Make-Up")
    mlist[2].append("Massage")
    mlist[2].append("Nail Salons")
    mlist[2].append("Pedicures")
    mlist[2].append("Perfume")
    mlist[2].append("Skin Care")
    mlist[2].append("Tanning Salons")
    mlist[2].append("Tattoos")
    mlist[2].append("Wigs")

    #mlist.append("Churches")
    mlist[3].append("Anglican Churches")
    mlist[3].append("Baptist Churches")
    mlist[3].append("Catholic Churches")
    mlist[3].append("Church of Jesus Christ of Latter Day Saints")
    mlist[3].append("Episcopalian Churches")
    mlist[3].append("Evangelical Churches")
    mlist[3].append("Jehovah's Witnesses")
    mlist[3].append("Lutheran Churches")
    mlist[3].append("Methodist Churches")
    mlist[3].append("Pentecostal Churches")
    mlist[3].append("Presbyterian Churches")
    mlist[3].append("Seven Day Adventist Churches")
    mlist[3].append("Synagogues")
    mlist[3].append("Temples")
    mlist[3].append("United Baptist Churches")

    #mlist.append("Computers")
    mlist[4].append("Computer Consultants")
    mlist[4].append("Computer Games")
    mlist[4].append("Computer Networking")
    mlist[4].append("Computer Rental")
    mlist[4].append("Computer Repair")
    mlist[4].append("Computer Stores")
    mlist[4].append("Internet Access")
    mlist[4].append("Video Games")
    mlist[4].append("Web Design")
    
    #mlist.append("Diet & Health")
    mlist[5].append("Diet Foods")
    mlist[5].append("Nutritionists")
    mlist[5].append("Vitamins")
    mlist[5].append("Weight Loss")        
    
    #mlist.append("Electronics")
    mlist[6].append("Cable TV")
    mlist[6].append("Cameras")
    mlist[6].append("Cell Phones")
    mlist[6].append("Digital Cameras")
    mlist[6].append("Electronics Stores")
    mlist[6].append("HiFi")
    mlist[6].append("Home Theater")
    mlist[6].append("Phones")
    mlist[6].append("Satellite TV")
    
    #mlist.append("Entertainment")
    mlist[7].append("Adult Entertainment")
    mlist[7].append("Art Galleries")
    mlist[7].append("Ballet")
    mlist[7].append("Bingo")
    mlist[7].append("Casinos")
    mlist[7].append("DVD Rental")
    mlist[7].append("Escort Services")
    mlist[7].append("Movie Rental")
    mlist[7].append("Movie Theaters")
    mlist[7].append("Museums")
    mlist[7].append("Night Clubs")
    mlist[7].append("Orchestras")
    mlist[7].append("Stage Theaters")

    #mlist.append("Finance")
    mlist[8].append("Accountants")
    mlist[8].append("Auto Loans")
    mlist[8].append("Banks")
    mlist[8].append("Bookkeeping")
    mlist[8].append("Check Cashing")
    mlist[8].append("Credit Cards")
    mlist[8].append("Credit Counseling")
    mlist[8].append("Credit Reports")
    mlist[8].append("Credit Unions")
    mlist[8].append("Estate Planning")
    mlist[8].append("Financial Planning")
    mlist[8].append("Home Loans")
    mlist[8].append("Investment Advisors")
    mlist[8].append("Mortgages")
    mlist[8].append("Motorcycle Loans")
    mlist[8].append("Mutual Funds")
    mlist[8].append("Personal Loans")
    mlist[8].append("Stock Brokers")
    mlist[8].append("Student Loans")
    mlist[8].append("Tax Preparation")
    mlist[8].append("Wealth Management")    

    #mlist.append("Fitness")
    mlist[9].append("Aerobics")
    mlist[9].append("Exercise Equipment")
    mlist[9].append("Fitness Centers")
    mlist[9].append("Fitness Clothing")
    mlist[9].append("Gyms")
    mlist[9].append("Health Clubs")
    mlist[9].append("Personal Trainers")
    mlist[9].append("Pilates")
    mlist[9].append("Yoga")    
    
    #mlist.append("Home")
    
    mlist[10].append("Antiques")
    mlist[10].append("BBQ")
    mlist[10].append("Beds")
    mlist[10].append("Blinds")
    mlist[10].append("Building Contractors")
    mlist[10].append("Cabinets")
    mlist[10].append("Carpenters")
    mlist[10].append("Carpet Cleaning")
    mlist[10].append("Closets")
    mlist[10].append("Contractors")
    mlist[10].append("Curtains")
    mlist[10].append("Electricians")
    mlist[10].append("Fencing")
    mlist[10].append("Fireplaces")
    mlist[10].append("Flooring")
    mlist[10].append("Furniture")
    mlist[10].append("Garage Doors")
    mlist[10].append("Garden Centers")
    mlist[10].append("Granite")
    mlist[10].append("Hardware")
    mlist[10].append("Heaters")
    mlist[10].append("Hot Tubs")
    mlist[10].append("House Cleaning")
    mlist[10].append("Insulation")
    mlist[10].append("Interior Design")
    mlist[10].append("Kitchen Appliances")
    mlist[10].append("Landscaping")
    mlist[10].append("Lighting")
    mlist[10].append("Locksmith")
    mlist[10].append("Lumber")
    mlist[10].append("Marble")
    mlist[10].append("Paint")
    mlist[10].append("Paving Contractors")
    mlist[10].append("Picture Framing")
    mlist[10].append("Plumbers")
    mlist[10].append("Refrigerators")
    mlist[10].append("Remodeling")
    mlist[10].append("Roofing")
    mlist[10].append("Sand & Gravel")
    mlist[10].append("Storage")
    mlist[10].append("Swimming Pool Service")
    mlist[10].append("Upholstery")
    mlist[10].append("Windows")    
    
    #mlist.append("Insurance")
    mlist[11].append("Accident Insurance")
    mlist[11].append("Auto Insurance")
    mlist[11].append("Boat Insurance")
    mlist[11].append("Business Insurance")
    mlist[11].append("Dental Insurance")
    mlist[11].append("Disability Insurance")
    mlist[11].append("Flood Insurance")
    mlist[11].append("Health Insurance")
    mlist[11].append("Home Insurance")
    mlist[11].append("Life Insurance")
    mlist[11].append("Motorcycle Insurance")
    mlist[11].append("Motorhome Insurance")
    mlist[11].append("Renters Insurance")
    mlist[11].append("Travel Insurance")

    #mlist.append("legal")
    mlist[12].append("Adoption Lawyers")
    mlist[12].append("Arbitration")
    mlist[12].append("Bankruptcy Lawyers")
    mlist[12].append("Business Lawyers")
    mlist[12].append("Child Custody Lawyers")
    mlist[12].append("Civil Rights Lawyers")
    mlist[12].append("Copyright Lawyers")
    mlist[12].append("Criminal Defense Lawyers")
    mlist[12].append("Divorce Lawyers")
    mlist[12].append("DUI Lawyers")
    mlist[12].append("Family Lawyers")
    mlist[12].append("Immigration Lawyers")
    mlist[12].append("Lawyers")
    mlist[12].append("Litigation Lawyers")
    mlist[12].append("Malpractice Lawyers")
    mlist[12].append("Mediation")
    mlist[12].append("Notaries")
    mlist[12].append("Patent Lawyers")
    mlist[12].append("Personal Injury Lawyers")
    mlist[12].append("Probate")
    mlist[12].append("Product Liability Lawyers")
    mlist[12].append("Real Estate Lawyers")
    mlist[12].append("Tax Lawyers")
    mlist[12].append("Trademark Lawyers")
    mlist[12].append("Trial Lawyers")
    mlist[12].append("Trusts")
    mlist[12].append("Wills")
    mlist[12].append("Accident Lawyers")
    
    #mlist.append("Lessons & Training")
    mlist[13].append("Computer Training")
    mlist[13].append("Dance Lesson")
    mlist[13].append("French Lesson")
    mlist[13].append("Golf Lesson")
    mlist[13].append("Guitar Lesson")
    mlist[13].append("Karate")
    mlist[13].append("Kickboxing")
    mlist[13].append("Kung Fu")
    mlist[13].append("Martial Arts")
    mlist[13].append("Music Lesson")
    mlist[13].append("Swimming Lesson")
    mlist[13].append("Tai Chi")
    mlist[13].append("Tutoring")
    mlist[13].append("Violin Lesson")
    
    #mlist.append("Markets")
    mlist[14].append("Bakery")
    mlist[14].append("Butcher")
    mlist[14].append("Convenience Store")
    mlist[14].append("Deli")
    mlist[14].append("Fish Market")
    mlist[14].append("Grocery Store")
    mlist[14].append("Liquor Store")
    
    #mlist.append("Medical")
    mlist[15].append("Chiropractic Clinics")
    mlist[15].append("Contact Lenses")
    mlist[15].append("Dental Clinics")
    mlist[15].append("Hearing Aids")
    mlist[15].append("Hospitals")
    mlist[15].append("Medical Clinics")
    mlist[15].append("Prosthetics")
    mlist[15].append("Wheelchairs")        
    mlist[15].append("Acupuncture")
    mlist[15].append("Anesthesiology")
    mlist[15].append("Cardiology")
    mlist[15].append("Chiropractors")
    mlist[15].append("Dentists")
    mlist[15].append("Dermatologists")
    mlist[15].append("Endocrinology")
    mlist[15].append("Gastroenterology")
    mlist[15].append("Gynecology")
    mlist[15].append("Hematology")
    mlist[15].append("Holistic Medicine")
    mlist[15].append("Homeopathy")
    mlist[15].append("Hypnotherapy")
    mlist[15].append("Immunology")
    mlist[15].append("Laser Eye Surgery")
    mlist[15].append("Massage Therapy")
    mlist[15].append("Naturopathy")
    mlist[15].append("Nephrology")
    mlist[15].append("Neurology")
    mlist[15].append("Obstetrics")
    mlist[15].append("Occupational Therapy")
    mlist[15].append("Oncology")
    mlist[15].append("Ophthalmology")
    mlist[15].append("Optometry")
    mlist[15].append("Orthodontics")
    mlist[15].append("Orthopedics")
    mlist[15].append("Orthotics")
    mlist[15].append("Osteopathy")
    mlist[15].append("Pathology")
    mlist[15].append("Pediatrics")
    mlist[15].append("Periodontics")
    mlist[15].append("Pharmacies")
    mlist[15].append("Physical Therapy")
    mlist[15].append("Plastic Surgery")
    mlist[15].append("Podiatry")
    mlist[15].append("Prosthodontics")
    mlist[15].append("Psychiatry")
    mlist[15].append("Psychology")
    mlist[15].append("Radiology")
    mlist[15].append("Reflexology")
    mlist[15].append("Rheumatology")
    mlist[15].append("Speech Pathology")
    mlist[15].append("Sports Medicine")
    mlist[15].append("Urology")

    #mlist.append("Movers & Storage")
    mlist[16].append("Business Records Storage")
    mlist[16].append("Full Service Storage")
    mlist[16].append("Household Storage")
    mlist[16].append("Movers")
    mlist[16].append("Moving Boxes")
    mlist[16].append("Packing")
    mlist[16].append("Packing Materials")
    mlist[16].append("Packing Supplies")
    mlist[16].append("Piano Movers")
    
    #mlist.append("Office Products & Supplies")
    mlist[17].append("Office Equipment")
    mlist[17].append("Office Equipment Rental")
    mlist[17].append("Office Furniture")
    mlist[17].append("Office Furniture Rental")
    mlist[17].append("Office Supplies")
    mlist[17].append("Used Office Equipment")
    mlist[17].append("Used Office Furniture")
    
    #mlist.append("Pets & Animals")
    
    mlist[18].append("Animal Hospitals")
    mlist[18].append("Animal Removal")
    mlist[18].append("Animal Shelters")
    mlist[18].append("Cat Sitting")
    mlist[18].append("Dog Sitting")
    mlist[18].append("Dog Training")
    mlist[18].append("Dog Walkers")
    mlist[18].append("Kennels")
    mlist[18].append("Pet Boarding")
    mlist[18].append("Pet Cemeteries")
    mlist[18].append("Pet Crematoriums")
    mlist[18].append("Pet Daycare")
    mlist[18].append("Pet Grooming")
    mlist[18].append("Pet Supplies")
    mlist[18].append("Pet Toys")
    mlist[18].append("Pet Training")
    mlist[18].append("Pet Walking")
    mlist[18].append("Veterinarians")
    
    #mlist.append("Professional Services")
    mlist[19].append("Architects")
    mlist[19].append("Career Counseling")
    mlist[19].append("Civil Engineers")
    mlist[19].append("Collection Agencies")
    mlist[19].append("Dry Cleaning")
    mlist[19].append("Electrical Engineers")
    mlist[19].append("Employment Agencies")
    mlist[19].append("Engravers")
    mlist[19].append("Executive Search Firms")
    mlist[19].append("Heating Engineers")
    mlist[19].append("Job Training")
    mlist[19].append("Laundry")
    mlist[19].append("Mechanical Engineers")
    mlist[19].append("Messenger Service")
    mlist[19].append("Musicians")
    mlist[19].append("Photocopying")
    mlist[19].append("Photographers")
    mlist[19].append("Piano Tuning")
    mlist[19].append("Printers")
    mlist[19].append("Private Investigators")
    mlist[19].append("Recording Studios")
    mlist[19].append("Resume Service")
    mlist[19].append("Signs")
    mlist[19].append("Structural Engineers")
    mlist[19].append("Tailor")
    mlist[19].append("Temp Agencies")
    mlist[19].append("Video Editing")
    mlist[19].append("Waste Management")
    
    #mlist.append("Real Estate")
    mlist[20].append("Apartments")
    mlist[20].append("Condos")
    mlist[20].append("Home Appraisals")
    mlist[20].append("Home Inspection")
    mlist[20].append("Real Estate Agents")
    mlist[20].append("Real Estate Brokers")
    mlist[20].append("Real Estate Consultants")
    mlist[20].append("Real Estate Developers")
    mlist[20].append("Real Estate Investments")
    mlist[20].append("Real Estate Management")
    mlist[20].append("Surveyors")
    
    #mlist.append("Recreation & Sports")
    mlist[21].append("Ammunition")
    mlist[21].append("Archery")
    mlist[21].append("Art Supplies")
    mlist[21].append("Billiards")
    mlist[21].append("Boating")
    mlist[21].append("Bowling")
    mlist[21].append("Camping")
    mlist[21].append("Charter Buses")
    mlist[21].append("Craft Shops")
    mlist[21].append("Cycling")
    mlist[21].append("Diving Equipment")
    mlist[21].append("Embroidery")
    mlist[21].append("Fishing")
    mlist[21].append("Flying Lessons")
    mlist[21].append("Golf Courses")
    mlist[21].append("Golf Driving Ranges")
    mlist[21].append("Golf Instruction")
    mlist[21].append("Gunsmiths")
    mlist[21].append("Hobby Shops")
    mlist[21].append("Horse Riding")
    mlist[21].append("Horse Stables")
    mlist[21].append("Hunting")
    mlist[21].append("Miniature Golf")
    mlist[21].append("Paintball")
    mlist[21].append("Photographic Equipment")
    mlist[21].append("Public Swimming Pools")
    mlist[21].append("Race Tracks")
    mlist[21].append("Skating")
    mlist[21].append("Skating Rinks")
    mlist[21].append("Ski Schools")
    mlist[21].append("Snowboards")
    mlist[21].append("Snowmobiles")
    mlist[21].append("Sporting Goods")
    mlist[21].append("Tennis Clubs")
    mlist[21].append("Tennis Lessons")

    #mlist.append("Schools")
    mlist[22].append("Acting Schools")
    mlist[22].append("Acupuncture Schools")
    mlist[22].append("Adult Education")
    mlist[22].append("Art Schools")
    mlist[22].append("Beauty Schools")
    mlist[22].append("Colleges")
    mlist[22].append("Community Colleges")
    mlist[22].append("Computer Schools")
    mlist[22].append("Continuing Education")
    mlist[22].append("Culinary Schools")
    mlist[22].append("Dental Schools")
    mlist[22].append("Drama Schools")
    mlist[22].append("Driving Schools")
    mlist[22].append("Elementary Schools")
    mlist[22].append("Engineering Schools")
    mlist[22].append("Fashion Schools")
    mlist[22].append("Film Schools")
    mlist[22].append("High Schools")
    mlist[22].append("Language Schools")
    mlist[22].append("Law Schools")
    mlist[22].append("Massage Schools")
    mlist[22].append("Paralegal Schools")
    mlist[22].append("Private Schools")
    mlist[22].append("Real Estate Schools")
    mlist[22].append("Secondary Schools")
    mlist[22].append("Technology Schools")
    mlist[22].append("Traffic Schools")
    mlist[22].append("Veterinary Schools")
    
    #mlist.append("Shopping")
    mlist[23].append("Baby Stores")
    mlist[23].append("Bed Stores")
    mlist[23].append("Bookstores")
    mlist[23].append("Candy Stores")
    mlist[23].append("Children's Clothing")
    mlist[23].append("Department Stores")
    mlist[23].append("Discount Stores")
    mlist[23].append("Drug Stores")
    mlist[23].append("Fabric Stores")
    mlist[23].append("Factory Outlets")
    mlist[23].append("Florists")
    mlist[23].append("Games")
    mlist[23].append("Gift Shops")
    mlist[23].append("Handbags")
    mlist[23].append("Jewelry")
    mlist[23].append("Leather Goods")
    mlist[23].append("Lingerie")
    mlist[23].append("Maternity Stores")
    mlist[23].append("Mattress Stores")
    mlist[23].append("Men's Clothing")
    mlist[23].append("Musical Instruments")
    mlist[23].append("Outlet Stores")
    mlist[23].append("Pawn Shops")
    mlist[23].append("Shoe Stores")
    mlist[23].append("Stationery")
    mlist[23].append("Thrift Stores")
    mlist[23].append("Toys")
    mlist[23].append("Uniforms")
    mlist[23].append("Watches")
    mlist[23].append("Women's Clothing")
    
    #mlist.append("Transportation")
    mlist[24].append("Aircraft Charter")
    mlist[24].append("Airport Parking")
    mlist[24].append("Airport Shuttles")
    mlist[24].append("Airport Transportation")
    mlist[24].append("Boat Charter")
    mlist[24].append("Bus Charter")
    mlist[24].append("Bus Lines")
    mlist[24].append("Car Rental")
    mlist[24].append("Helicopter Charter")
    mlist[24].append("Limos")
    mlist[24].append("Taxicabs")
    mlist[24].append("Yacht Charter")    
    
    #mlist.append("Travel")
    mlist[25].append("Airlines")
    mlist[25].append("Airports")
    mlist[25].append("Bed & Breakfast")
    mlist[25].append("Cruises")
    mlist[25].append("Hotels")
    mlist[25].append("Luggage")
    mlist[25].append("Motels")
    mlist[25].append("Passport Photographers")
    mlist[25].append("Travel Agents")  
    
    return mlist

if __name__ == '__main__':
    main()