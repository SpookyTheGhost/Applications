print("Welcome to automated US sales taxes")

print("BEWARE: Delaware, Montana, New Hampshire, Oregon do not collect any sales tax!")

selectedState = print("Please select a single state based on initials: ")

print("""MENU
-------------------------------------------------------------------
Alabama:AL
Alaska:AK
Arizona:AZ
Arkansas:AR
California:CA
Colorado:CO
Connecticut:CT
Florida:FL
Georgia:GA
Hawaii:HI
Idaho:ID
Illinois:IL
Indiana:IN
Iowa:IA
Kansas:KS
Kentucky:KY
Louisiana:LA
Maine:ME
Maryland:MD
Massachusetts:MA
Michigan:MI
Minnesota:MN
Mississippi:MS
Missouri:MO
Nebraska:NE
Nevada:NV
New Jersey:NJ
New Mexico:NM
New York:NY
North Carolina:NC
North Dakota:ND
Ohio:OH
Oklahoma:OK
Pennsylvania:PA
Rhode Island:RI
South Carolina:SC
South Dakota:SD
Tennessee:TN
Texas:TX
Utah:UT
Vermont:VT
Virginia:VA
Washington:WA
West Virginia:WV
Wisconsin:WI
Wyoming:WY
D.C.:DC
""")

USstates = {AL:4.00, AK:0.00, AZ:5.60, AR:6.50, CA:7.25, CO:2.90, CT:6.35, FL:6.00, GA:4.00, HI:4.00, ID:6.00, IL:6.25, IN:7.00, IA:6.00, KS:6.50, KY:6.00, LA:5.00, ME:5.50, MD:6.00, MA:6.25, MI:6.00, MN:6.88, MS:7.00, MO:4.23, NE:5.50, NV:6.85, NJ:6.88, NM:5.13, NY:4.00, NC:4.75, ND:5.00, OH:5.75, OK:4.50, PA:6.00, RI:7.00, SC:6.00, SD:4.50, TN:7.00, TX:6.25, UT:5.95, VT:6.00, VA:5.30, WA:6.50, WV:6.00, WI:5.00, WY:4.00, DC:5.75}
Bill = float(input("Bill total: "))

# get the sales tax rate in percentage form
def percentage(selectedState):
	return (USstates[selectedState.upper()]/100.00)

print("your total is: ", Bill*=(1+percentage(selectedState)))

