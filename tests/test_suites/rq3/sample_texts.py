from app.classes.spec.symboleo_contract import SymboleoContract

# Might make a simpler symboleo contract convenience function for building up these examples


class SampleText:
    def __init__(self, text):
        self.text = text
        self.sym = ''


# BEFORE DATE
'the Franchise Fee shall be paid to Grantor on or before March 31, 2017.'

'In no event will Fox develop, publish and/or distribute games derived from the Property "ICE AGE 2" prior to January 1, 2007'

'COMWARE must purchase no less than $22,710.00 worth of Products, in any combination, by April 15, 2000'

'Grantor\'s percentage share shall be determined pursuant to this Section, and paid to Grantor on or before March 31 of the succeeding calendar year'

'If Ten (10) music venues sign a contract with VNUE before January 16, 2016}, ...'

'the Franchise Fee shall be paid to Grantor on or before March 31, 2017'

'Should any Participation Agreement(s) between Company and any Fund(s) be terminated effective before the last day of a quarter, ...'



# BEFORE TIMEPOINT

'Tickets may terminate this Agreement for any reason upon thirty (30) days\' notice to MP3. com at any time prior to the expiration of sixty (60) days subsequent to the Effective Date'

'Tickets agrees to pay MP3.com, during the term of this Agreement, as follows: (i) $[***] payable on the Effective Date; (ii) $[***] payable on or before one month subsequent to the Effective Date;'

'In the event the Company fails to have its attorney issue the required opinion letter within 20 days of a written request from YourNetPlus.com or its nominee'

'the parties shall act in a commercially reasonable manner and speedily select and then conduct the arbitration within 45 days with the expenditure of minimal discovery efforts and expense'

'the Fund shall make such payment within 30 days after each month-end'

'Dolphin agrees to complete its photo-editing services within 14 days of receiving the original digital photo files'

'The Services are deemed to be accepted if MMI does not receive a notification within 60 days after delivery to Dragon Systems or its customers'

'Payments will be due in US dollars within 30 days after delivery'
# Payments will be due in US dollars within 30 days after delivery, or when agreed after delivery of installments or the receipt of invoice by Dragon Systems, which ever is later

'Should MMI not supply the Services as agreed or should the Services become defective within 6 months from their delivery to Dragon Systems'

'All undisputed Royalty payments shall be made in U.S. dollars in cash or to the order of Individual and shall be due and payable within thirty (30) days after the end of each calendar month for sales during the previous month'

'If you do not make the extra payment within 60 days from the date we notify you of your share of the deficiency...'

'The seller shall be confirmed within three working days after receipt of order'

'The Buyer shall open an irrevocable letter of credit with the bank within 30 days after signing the contract, in favor of the Seller, for 100% value of the total contract value'

'The seller shall within 72 hours after the shipment of the goods, advise the shipping department of buyer by fax or E-mail of Contract No., goods name, quantity, value, number of packages, gross weight, measurements and the estimated arrival time of the goods'

'If the Sellers fail to answer the Buyers within one weeks after receipt of the aforesaid claim...'



## TIMESPAN BEFORE -> Date.add(-val, X)
'SLD shall submit third party display materials at least five days prior to the event for ACM\'s approval'

'Display materials from the Sponsor must be delivered to the Tian He Stadium at least two days prior to the event.'

'This agreement shall renew automatically each year thereafter, unless either party serves written notice of its intention not to renew, on the other at least 90 days prior to the expiration of the then current term of this agreement'

'In case the goods are to be dispatched by parcel post/sea-freight, the Sellers shall, 3 days before the time of delivery, inform the Buyers by cable/letter of the estimated date of delivery, Contract No., commodity, invoiced value, etc'




# BEFORE EVENT

## Before
'the Equipment must be delivered to, and accepted by, the Company on or before the Last Delivery Date specified in Section 2:05'

'On or before the Lease Commencement Date for any Schedule, the Company shall present to Lessor documentation ("Purchase Documentation")'

'The orders become effective once the seller accepts, any party shall not unilaterally cancel the order before the two sides agreed'

## by the time

## prior to
'General Electric Capital Corporation will also require a complete set of Lease documentation prior to funding'

'Porex shall bear the costs of any expenses incurred prior to formal written agreement of the Statement of Work'

'the parties shall agree to a proposed sales price for use during the project in writing prior to the commencement of each project'

'Either Party may terminate this Agreement at any time prior to delivery of the Product'

'It is Client\'s sole responsibility to check the accuracy of the written content and correct any errors prior to submission for final publication'

'Distributor shall obtain an RMA number prior to returning any Product to Cisco'


# AFTER EVENT

## AFTER
'ITS will deliver working systems no later than 30 days after a hard           copy purchase order is received from COMWARE'
### "no later than" ~ "within 30 days of"... note this

### Many cases include within TIMESPAN after - these are false positives. Need to filter them out

'Maimon also covenants that at any time after the termination of this Agreement, directly or indirectly, he will not use any Confidential Information or divulge or disclose any Confidential Information to any person'
### This one feels more like a conditional

'DGT shall be entitled to terminate this Agreement if Dolphin fails to meet its requirements and material obligation hereunder and only after DGT have given Dolphin written notice of such failure'
### Another conditional

'If dividends are credited after premiums can no longer be paid under this contract, dividends will be paid in cash'
### Maybe this works

'if Distributor places Purchase Orders after the expiration of the Agreement'

'Each party agrees that after the delivery of this Agreement it or he will execute and deliver such further documents '

'After Fox or its assigns deducts its Distribution Fee, it shall remit the remainder to Licensee '

'The sellers shall, immediately after dispatch of the goods, advise the Buyers by cable/letter of the Contract No'

## Following
'the non-defaulting party shall have the right to terminate this Agreement following the expiration of such 30-day notice period.'


'payment to Porex of undisputed fees shall be due [*] days following Cerus\' receipt of the invoice submitted by Porex'
## This is a point function... TIMESPAN AFTER - its actually a before TIMESPAN after (i think)



# HappensAfter (looking for date or point_function)

'other party\'s material breach that remains not cured and continues for a period of (A) in the case of a failure involving the payment of any undisputed amount due hereunder, 15 days and (B) in the case of any other failure, 30 days after the non performing party receives notice from the terminating party specifying such failure'
# point func

'the Company shall have the option of canceling this Agreement following the passage of ten  (10) days after having given Cano written notice of its default'
## point func following TIMESPAN after EVENT
## awkward..

'Licensee\'s right and license to develop and distribute the Game in connection with the Property "ICE AGE 2" shall become non-exclusive after December 31, 2006.'

'Licensee\'s right and license to distribute the KOH Video Clips shall expire twelve (12) months after the initial theatrical release of the Property "KINGDOM OF HEAVEN".'


# following may have some bearing on durations....
'KCI pledges that it will not circumvent the relationships among venders, providers and clients developed by Provider either directly or indirectly, during the contract period and for a period of up to 2 (two) years following termination of this contract'

'During the Term and any renewal terms of the Agreement, and for a period of one (1) year following the expiration or earlier termination thereof, Customer agrees not to work with, directly or indirectly, any Third-Party that Customer comes to know through disclosure by Kubient as part of the Services'

'for a period of one (1) year following the expiration or earlier termination thereof, Customer agrees not to work with, directly or indirectly, any Third-Party that Customer comes to know through disclosure by Kubient'

'For a period of five (5) years after termination of this Agreement, the parties shall treat as confidential all information'

## Happens After is hard 


# HappensWithin

## Between
'Any notice mailed as aforesaid shall be deemed to have been received on the expiration of five days after it is posted, provided that if there shall be at the time of mailing or between the time of mailing and the actual receipt of the notice a mail strike, slow down or labour dispute which might affect the delivery of the notice by the mails'

'If the Agreement expired prior to the Amendment Effective Date, any orders received and Products and Services purchased between the date of expiration and the Amendment Effective Date shall be in all respects deemed made under the Agreement as in effect prior to this Amendment.'


## During
'KCI pledges that it will not circumvent the relationships among venders, providers and clients developed by Provider either directly or indirectly, during the contract period '

'COMWARE must purchase order a minimum      of $4,200 worth of Products per month during the Renewal Period'

'Company shall have unlimited rights of utilization of the           Professional\'s Image in all advertising, promotion, publicity and           other forms of communication with any part during the term of this           Agreement'
# During this agreement - may be redundant...

'Porex will invoice Cerus monthly for Services performed by Porex during the prior month'

'During the initial one year period beginning on the Amendment Date,          Distributor shall be the only distributor appointed by NETGEAR'
# More of a situation

'Member shall not, during the term of the Franchise Agreement or thereafter, communicate, divulge or use, for any purpose other than the operation of the Franchised Business, any confidential information, knowledge, trade secrets or know-how'

'During the initial Maintenance Term and any renewal term, Maintenance Fees shall be paid in the increments described below under "Payment Terms."'

'During the transportation, Part B shall completely comply with Party A\'s transportation arrangement and relevant systems'


# TRIGGER

## When
### Lots of "when necessary" - not meaningful
'Payments will be due in US dollars within 30 days after delivery, or when agreed after delivery of installments or the receipt of invoice by Dragon Systems, which ever is later'

'When custom Products are designed, developed and to be delivered to Bravatek-identified perspective clients, the parties shall agree to a proposed sales price for use during the project in writing prior to the commencement of each project.'

'When the Agreement ends, each party shall return all copies of any such information to the other and take every reasonable measure to preclude its representatives from sharing or keeping such information'

'All notices, requests, demands, and other communications required or permitted hereunder will be in writing and will be deemed to have been duly given when delivered by hand, by overnight courier, or fax'


# ANTECEDENT

## IF
'If any provision of this Agreement shall be invalid or unenforceable, such invalidity or unenforceability shall not render the entire Agreement invalid'

'If the ISP does not have 250 users within the first 90 days we will charge $25.00 each month thereafter'

'If the Fund\'s Net Investment Income on any day is below zero, the Investment  Adviser shall waive its Advisory Fee or reimburse the Fund an amount (defined as "Expense Waiver") sufficient to produce a Net  Investment Income of zero'

'If the Investment Adviser is required to reimburse the Fund, the Investment Adviser shall make such payment within 30 days  after each month-end in the amount due the Fund as of each month'

'If Porex begins to perform services under a work order that has not been formally agreed in writing, then Porex shall bear the costs of any expenses incurred prior to formal written agreement of the Statement of Work'

'If Tickets reasonably disputes the Count pursuant to this Agreement, then Tickets shall have the right to select the independent auditor of its choice to conduct an audit of MP3.com\'s records (the "Audit")'

'If you believe that the Company has billed you incorrectly, you must contact Company no later than 60 days after the closing date on the first billing statement in which the error or problem appeared'

'If any provision of this Agreement shall be held invalid or unenforceable by a court or regulatory body of competent jurisdiction, the remainder of this Agreement shall remain in full force and effect'

'The Services are deemed to be accepted if MMI does not receive a notification within 60 days after delivery to Dragon Systems or its customers'

'If any legal action is brought by either of the parties hereto, it is expressly agreed that the prevailing party in such legal  action shall be entitled to recover from the other party reasonable attorney\'s fees in addition to any other relief that may be awarded'

' If Cano fails to make any  payment when required by this Agreement, the Company shall have the option of canceling this Agreement following the passage of ten  (10) days after having given Cano written notice of its default'

'If Lucent determines that mPhase\'s Goods are no longer maintained at          the current level of quality, Lucent shall so notify mPhase, in          writing, and Lucent shall have the right to terminate this Agreement'

'If the solvency of the Society becomes impaired, you may be required to make an extra payment'

'If Distributor is a non-governmental entity, it will notify Cisco In writing lf any of its owners, partners, principals, officers, or employees are or become, during the term of this Agreement, officials, officers or representatives of any government, political party'

'Cisco may terminate this Agreement immediately upon written notice if Distributor breaches any of the representations and warranties set forth in this section'

'If any action is brought among the parties with respect to this Agreement or otherwise, by way of a claim or counterclaim, the parties agree that in any such action, and on all issues, the parties irrevocably waive their right to a trial by jury.'

'If Bank of America terminates the Maintenance Services, Bank of America shall have the right to reinstate the Maintenance Services without paying any reinstatement fee'

'If Ten (10) music venues sign a contract with VNUE before January 16, 2016, Promoter will receive an additional bonus of Three Hundred Thousand (300,000) shares of VNUE common stock'

'If the seller puts forward amendments or not accept orders, the seller shall be in the form of a written notice to entrusted party, entrusted party accept the modified by written consent, the modified orders to be taken effect'

'If the Sellers fail to answer the Buyers within one weeks after receipt of the aforesaid claim, the claim shall be reckoned as having been accepted by the Sellers'

## UPON
'Any notice, instruction, direction or demand under the terms of this Agreement required to be in writing shall be duly given upon delivery,'

'Upon the effective date of this agreement COMWARE shall have the exclusive right to purchase, at the DISCOUNTS described below'

' This Agreement will terminate upon the termination of the Advisory Agreement'

'Upon Cerus\' determination that the Protocol EPP-029- 886 can be discontinued, Cerus shall provide written notice thereof to Porex'

'Upon approval by Cerus of the corrective plan, Porex, at no additional expense to Cerus, shall then make the corrections and, where applicable, Porex shall resubmit the corrected Services to Cerus'

'Tickets may terminate this Agreement for any reason upon thirty (30) days\' notice to MP3'

'Upon request, Tickets shall have access to pertinent statistics related to Impressions covering the period of this contract'

'Such reimbursements shall be made by the Operating Company to EmployeeCo in advance or immediately upon such costs being incurred'

'Upon termination of this Agreement, Maimon agrees to return immediately to the Company all written Confidential Information '

'Upon reasonable request, copies of any such books and records shall be provided promptly by FASC to the Account or the Account\'s owners or authorized representatives.'

'Upon completion of a transaction, the transaction settlement group works with the broker and the account custodian to ensure timely and accurate exchange of securities and monies'

' the Royalty will cease being paid upon the death of Individual'

'Upon the signing of this Agreement, Client agrees to pay to Company a total of $5,000.'


## ONCE
'Once the common stock has been registered, or, after the one year period applicable under Rule 144, whichever occurs first, the Company at its sole cost and expense have its attorney issue an opinion letter for removal of the legend'

'Both Parties agree that once the Parties have agreed to transaction which includes the purchase and sale of the Product that the Buyer will remit payment upon execution of this agreement'

'Once the payment has been received, Shi Farms will use its best efforts to quarantine product to ensure safe keeping of the Product until delivery date as agreed by the Parties.'


## IN EVENT
'in the event of a conflict between the terms of this Agreement and the Lease, the Lease shall control'

'In the event the Company is in default hereunder or under the Lease, Lessor may elect to terminate this Agreement immediately'

'In the event  either of these dates are not met,        this Agreement will automatically and immediately terminate and neither        of the parties  hereto will have any  further  obligations,  one to the        other.'

'In the event COMWARE purchases  products in excess of $45,420.00 during          the  Initial  Distribution  Period, COMWARE  shall  have  the  right to          purchase additional Products at the following discounts'

'In the event COMWARE  purchases an amount less than      $45,420.00, than this Agreement will automatically terminate.'

'In event of cancellation of a purchase order, or re-scheduling of any           item on a purchase order beyond the discount period, COMWARE may be           liable for bill back or adjustment of discounts based upon actual           quantities of items delivered within the discount period.    '

'In the event the           Professional should for any reason become a non-exempt PGA Tour player,          the Company shall have the right to terminate this Agreement at its          discretion at any time during the initial term or any extension           thereof.'

'Dolphin shall be entitled to defer any obligation hereunder in the event of force majeure'

'In the event such notice is given, the Adviser shall assume the defense of the claim, and FASC shall cooperate with the Adviser in such defense, subject to the obligation of the Adviser to reimburse FASC for the expenses resulting therefrom. In the event Adviser gives notice that it'

'In the event that mPhase\'s use of the Lucent Co-Branding Logo, in the          sole judgment of Lucent, may adversely affect Lucent\'s rights to the          mark shown on Schedule A or the marks and names LUCENT'

'In the event that mPhase becomes aware of any unauthorized use of the          Lucent Co-Branding Logo or other Lucent marks by third parties, mPhase          agrees to promptly notify Lucent and to cooperate fully, at Lucent\'s          expense, in any enforcement of Lucent\'s rights against'

'In the event of termination, the Distributor shall be entitled to receive all orders accepted by the Principal prior to the date of termination and may sell the ordered Products in the Territory.'

'In the event of parcel damage resulting from leakage or fire, Party B shall indemnify at the standard rate of RMB200 per parcel'

'In the event the vehicle space insufficiency which causes Party A\'s need unable to be satisfied nor can it be adjusted to satisfy Party A\'s need, Party A can terminate this Agreement without any compensation'


## IN CASE
'In case any provision of this Agreement shall be invalid, illegal or unenforceable, the validity, legality and enforceability of the remaining provisions of the Agreement shall not in any way be affected or impaired thereby'

'In case the goods are to be dispatched by parcel post/sea-freight, the Sellers shall, 3 days before the time of delivery, inform the Buyers by cable/letter of the estimated date of delivery, Contract No., commodity, invoiced value, etc'

'In case the accident lasts for more than 10 weeks, the Buyers shall have the right to cancel the Contract'

'In case the Sellers fail to make delivery ten weeks later than the time of shipment stipulated in the Contract, the Buyers have the right to cancel the contract '

'In case no settlement can be reached, the case may then be submitted for arbitration to the Foreign Economic and Trade Arbitration Committee of the China Beijing Council for the Promotion of International Trade'



# DOMAIN

## By inst
'if delivered by hand'

'if sent by facsimile transmission'

'approved by a majority of the shareholders of each Portfolio of  the Series Fund on October 21'

'All notices required or permitted under this Agreement must be in writing and delivered by email or personal delivery on the date sent'

## With
'the goods must be marked with the IPPC stamps, which are certified by the government agent of Botanical-Inspection and Quarantine Bureau'

'The Sellers shall mark on each package with fadeless paint the package number, gross weight, net weight, measurements and the wordings'



## using
'Porex shall continue to manufacture and produce Platelet Wafers using the existing specifications for Platelet Wafers'




# UNLESS UNTIL

## UNLESS
'Unless otherwise agreed in writing, Porex shall continue to manufacture and produce Platelet Wafers using the existing specifications for Platelet Wafers until Cerus gives written notice to Porex that Platelet Wafers shall be thereafter manufactured in accordance with the Revised Wafer Specifications'
## Has both!
# porex shall continue to manufacture --- situation..
# Obligation: situation S must hold unless event X
# create a trigger: event X => power to suspend the obligation ... power would go to the OTHER role


'Unless otherwise expressly provided in the applicable Statement of Work payment to Porex of undisputed fees shall be due [*] days following Cerus\' receipt of the invoice submitted by Porex'
# Payment is due unless.
# event E must happen unless event X
# creates a trigger: event X => power to suspend obligation

'the Agreement shall control unless the Statement of Work expressly refers to the Parties\' intent to alter the terms of the Agreement '
# if statement of work refers THEN agreement shall not control

'this Service Agreement is for the total duration of the Company\'s Offering (the "Initial Term") unless either party requests termination'
# if party requests termination ==> then what happens? under-specified.. 

'Maimon will not, unless expressly authorized in writing by the Company, at any time use any Confidential Information or divulge or disclose any Confidential Information to any person'
# initial: O(maimon, other, t, not Happens(divulge_info))
# authorized in writing ==> power to suspend

'BOSCH reserves the right to share rights given unless it disrupts and/or interferes with CLIENTS business and/or productivity.'
# initial: its a right, so nothing really?
# disrupts => right is lost: O(bosch, other, t, not Happens(share_rights))
# tough one... can I frame it as suspension

'dividends will be applied under the Payment of Premium option unless the Cash option has been chosen in writing'
# initial: Obligation to apply dividends
# cash option chosen => suspend it


'Unless accepted by the Principal, the Distributor agrees that during the term of this Agreement, the Distributor, either directly or indirectly, shall handle no products that are competitive with the Products within the Territory.'
# Interesting one
# initial: O(distributor, other, t, not Happens(handle_products))
# accepted => O(other, distributor, t, suspend(initial))
## This makes sense

'No supplement to or amendment of this Agreement will be binding unless executed in writing by LEADER and EZJR.'
# weirder one

'the Maintenance Term shall automatically renew for successive period, 12 months, on the terms and conditions of this Agreement unless Bank of America terminates Maintenance Services pursuant to this Agreement'
# renewal - a bit odd as well

'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract unless such delay exceeds 10 days'
# So many negations here... kinda tough
# initial... absence of a power... not needed?
# delay exceeds => power to terminate... Creates a power
## so its a tough one.
# non-power + unless => new power
# so can we capture this "non-power"... maybe as a never? And then reverse it?


## UNTIL
'The damages shall accrue until the transfer agent receives the opinion letter'
# situation UNTIL
## we would need to rep a situation - frame as event
## the damages shall accrue
## X may not prevent damages from accruing


'This Agreement shall remain in force until each component ofProject Completion is satisfied'
# situation

'Porex shall continue to manufacture and produce Platelet Wafers using the existing specifications for Platelet Wafers until Cerus gives written notice to Porex'
# situation
## reframe: obligation - porex shall not cease to manufacture wafers
## then we have an UNTIL EVENT
## that  will suspend the obligation

'This Agreement shall remain in effect until terminated by the Parties'
# situation


'Bioamber may fund the BRI Project up until the Methylotroph (or re-engineered Methylotroph) demonstrates  the ability to produce succinic acid'
# situation


'Shi Farms will use its best efforts to quarantine product to ensure safe keeping of the Product until delivery date as agreed by the Parties'
# situation
# reframe ob: O(shi, b, true, not Happens(unquarantine))
# delivery trigger => suspend


'This Agreement shall be in effect until March 18. 2021,'
# dates - this is a possibility

'shall have the exclusive right and license to develop and distribute until December 31, 2006'
# date
# situation until date... 


'The Letter of Credit shall be valid until 90 days after the latest shipment is effected'
# situation
# must not be invalidated until timespan after event
# Same thing


'The seller shall contract on usual terms at his own expenses for the carriage of the goods to the agreed point at the named place of destination and bear all risks and expenses until the goods have been delivered to the port of destination.'
# situation

# until can be framed as any timepoint - event, date, point_function
# party must not do event X until March 30
# not HappensBefore(eventX, march 30)

# what about an event
# partyA must not do event X until event Y
# initial: O(A,B, true, not Happens(eventX))
# until: O(A,B, true, not HappensBeforeEvent(eventX, eventY))
# ORRR: Happens(eventY) -> suspends it?
# 
# Its a situation that happens until a timepoint. Therefore it can be refined to a HappensBefore 

# what about a from and until. 
# situation X must hold from A until B. 

# must not disrupt situation X from A until B... still makes sense...

# situation X must hold until event Y
##  O(A,B, true, not HappensBeforeEvent(eventX, eventY))

# situation must hold from event W until event Y
## O(A, B, true, not HappensWithin())
## Yup, we're good

# must happen from March 


## WITHOUT...?