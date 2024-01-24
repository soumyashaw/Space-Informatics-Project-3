import datetime
import matplotlib.pyplot as plt

def mergeIntervals(listA, listB):
    mergedIntervals = []

    allIntervals = listA + listB
    
    allIntervals.sort(key=lambda x: x[0])
    
    currentInterval = allIntervals[0]
    
    for interval in allIntervals[1:]:
        if interval[0] <= currentInterval[1]:
            if (interval[1] - interval[0]) > (currentInterval[1] - currentInterval[0]):
                currentInterval = interval
        else:
            mergedIntervals.append(currentInterval)
            currentInterval = interval
    
    mergedIntervals.append(currentInterval)
    
    return mergedIntervals

def plot_intervals(intervals):
    fig, ax = plt.subplots()
    
    for start, end in intervals:
        ax.plot([start, end], [1, 1], marker='.', markersize=1, color='blue')
    
    ax.set_yticks([])
    ax.set_xlabel('Time')
    ax.set_title('Time Intervals')
    
    plt.show()

def has_coinciding_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] <= sorted_intervals[i - 1][1]:
            return True  # Coinciding intervals found

access_A = [(datetime.datetime(2026, 5, 27, 14, 43, 6, 471273), datetime.datetime(2026, 5, 27, 15, 1, 49, 238509)), (datetime.datetime(2026, 5, 27, 17, 0, 58, 235900), datetime.datetime(2026, 5, 27, 17, 19, 53, 901704)), (datetime.datetime(2026, 5, 27, 19, 18, 50, 30315), datetime.datetime(2026, 5, 27, 19, 37, 58, 286847)), (datetime.datetime(2026, 5, 27, 21, 36, 41, 857352), datetime.datetime(2026, 5, 27, 21, 56, 2, 384900)), (datetime.datetime(2026, 5, 27, 23, 54, 33, 722668), datetime.datetime(2026, 5, 28, 0, 14, 6, 199209)), (datetime.datetime(2026, 5, 28, 
2, 12, 25, 632986), datetime.datetime(2026, 5, 28, 2, 32, 9, 728878)), (datetime.datetime(2026, 5, 28, 4, 30, 17, 599834), datetime.datetime(2026, 5, 28, 4, 50, 12, 960964)), (datetime.datetime(2026, 5, 28, 6, 48, 9, 629034), datetime.datetime(2026, 5, 28, 7, 8, 15, 905307)), (datetime.datetime(2026, 5, 28, 9, 6, 1, 726680), datetime.datetime(2026, 5, 28, 9, 26, 18, 558009)), (datetime.datetime(2026, 5, 28, 11, 23, 53, 901285), datetime.datetime(2026, 5, 28, 11, 44, 20, 916288)), (datetime.datetime(2026, 5, 28, 13, 41, 46, 155967), datetime.datetime(2026, 5, 28, 14, 2, 22, 981252)), (datetime.datetime(2026, 5, 28, 15, 59, 38, 494419), datetime.datetime(2026, 5, 28, 16, 20, 24, 753462)), (datetime.datetime(2026, 5, 28, 18, 17, 30, 931833), datetime.datetime(2026, 5, 28, 18, 38, 26, 234101)), (datetime.datetime(2026, 5, 28, 
20, 35, 23, 468671), datetime.datetime(2026, 5, 28, 20, 56, 27, 425633)), (datetime.datetime(2026, 5, 28, 22, 53, 16, 108625), datetime.datetime(2026, 5, 28, 23, 14, 28, 327149)), (datetime.datetime(2026, 5, 29, 1, 11, 8, 863988), datetime.datetime(2026, 5, 29, 1, 32, 28, 941376)), (datetime.datetime(2026, 5, 29, 3, 29, 1, 737905), datetime.datetime(2026, 5, 29, 3, 50, 29, 276474)), (datetime.datetime(2026, 5, 29, 5, 46, 54, 734530), datetime.datetime(2026, 5, 29, 6, 8, 29, 325822)), (datetime.datetime(2026, 5, 29, 8, 4, 47, 858125), datetime.datetime(2026, 5, 29, 8, 26, 29, 93610)), (datetime.datetime(2026, 5, 29, 10, 22, 41, 115623), datetime.datetime(2026, 5, 29, 10, 44, 28, 588284)), (datetime.datetime(2026, 5, 29, 12, 40, 34, 515954), datetime.datetime(2026, 5, 29, 13, 2, 27, 807688)), (datetime.datetime(2026, 5, 29, 
14, 58, 28, 63295), datetime.datetime(2026, 5, 29, 15, 20, 26, 759975)), (datetime.datetime(2026, 5, 29, 17, 16, 21, 759297), datetime.datetime(2026, 5, 29, 17, 38, 25, 445281)), (datetime.datetime(2026, 5, 29, 19, 34, 15, 609364), datetime.datetime(2026, 5, 29, 19, 56, 23, 867524)), (datetime.datetime(2026, 5, 29, 21, 52, 9, 621742), datetime.datetime(2026, 5, 29, 22, 14, 22, 31360)), (datetime.datetime(2026, 5, 
30, 0, 10, 3, 802191), datetime.datetime(2026, 5, 30, 0, 32, 19, 942315)), (datetime.datetime(2026, 5, 30, 2, 27, 58, 155084), datetime.datetime(2026, 5, 30, 2, 50, 17, 599768)), (datetime.datetime(2026, 5, 30, 4, 45, 52, 685683), datetime.datetime(2026, 5, 30, 5, 8, 15, 10938)), (datetime.datetime(2026, 5, 30, 7, 3, 47, 395219), datetime.datetime(2026, 5, 30, 7, 26, 12, 181919)), (datetime.datetime(2026, 5, 30, 9, 21, 42, 294217), datetime.datetime(2026, 5, 30, 9, 44, 9, 112563)), (datetime.datetime(2026, 5, 30, 11, 39, 37, 382472), datetime.datetime(2026, 5, 30, 12, 2, 5, 813134)), (datetime.datetime(2026, 5, 30, 13, 57, 32, 670828), datetime.datetime(2026, 5, 30, 14, 20, 2, 280457)), (datetime.datetime(2026, 5, 30, 16, 15, 28, 162805), datetime.datetime(2026, 5, 30, 16, 37, 58, 527412)), (datetime.datetime(2026, 5, 30, 
18, 33, 23, 859810), datetime.datetime(2026, 5, 30, 18, 55, 54, 555734)), (datetime.datetime(2026, 5, 30, 20, 51, 19, 767302), datetime.datetime(2026, 5, 30, 21, 13, 50, 365461)), (datetime.datetime(2026, 5, 30, 23, 9, 15, 894345), datetime.datetime(2026, 5, 30, 23, 31, 45, 969212)), (datetime.datetime(2026, 5, 31, 1, 27, 12, 242513), datetime.datetime(2026, 5, 31, 1, 49, 41, 367567)), (datetime.datetime(2026, 5, 
31, 3, 45, 8, 815090), datetime.datetime(2026, 5, 31, 4, 7, 36, 562922)), (datetime.datetime(2026, 5, 31, 6, 3, 5, 616289), datetime.datetime(2026, 5, 31, 6, 25, 31, 564039)), (datetime.datetime(2026, 5, 31, 8, 21, 2, 657217), datetime.datetime(2026, 5, 31, 8, 43, 26, 374328)), (datetime.datetime(2026, 5, 31, 10, 38, 59, 934432), datetime.datetime(2026, 5, 31, 11, 1, 21, 3118)), (datetime.datetime(2026, 5, 31, 12, 56, 57, 459980), datetime.datetime(2026, 5, 31, 13, 19, 15, 448151)), (datetime.datetime(2026, 5, 31, 15, 7, 57, 770292), datetime.datetime(2026, 5, 31, 15, 30, 17, 547117)), (datetime.datetime(2026, 5, 31, 17, 25, 52, 319216), datetime.datetime(2026, 5, 31, 17, 48, 14, 934136)), (datetime.datetime(2026, 5, 31, 19, 43, 47, 52323), datetime.datetime(2026, 5, 31, 20, 6, 12, 77258)), (datetime.datetime(2026, 5, 31, 
22, 1, 41, 971669), datetime.datetime(2026, 5, 31, 22, 24, 8, 987453)), (datetime.datetime(2026, 6, 1, 0, 19, 37, 86131), datetime.datetime(2026, 6, 1, 0, 42, 5, 660405)), (datetime.datetime(2026, 6, 1, 2, 37, 32, 393504), datetime.datetime(2026, 6, 1, 3, 0, 2, 106731)), (datetime.datetime(2026, 6, 1, 4, 55, 27, 908203), datetime.datetime(2026, 6, 1, 5, 17, 58, 327833)), (datetime.datetime(2026, 6, 1, 7, 13, 23, 628633), datetime.datetime(2026, 6, 1, 7, 35, 54, 334420)), (datetime.datetime(2026, 6, 1, 9, 31, 19, 560124), datetime.datetime(2026, 6, 1, 9, 53, 50, 122953)), (datetime.datetime(2026, 6, 1, 11, 49, 15, 711348), datetime.datetime(2026, 6, 1, 12, 11, 45, 705579)), (datetime.datetime(2026, 6, 1, 14, 7, 12, 84063), datetime.datetime(2026, 6, 1, 14, 29, 41, 78661)), (datetime.datetime(2026, 6, 1, 16, 25, 8, 681730), 
datetime.datetime(2026, 6, 1, 16, 47, 36, 258633)), (datetime.datetime(2026, 6, 1, 18, 43, 5, 508399), datetime.datetime(2026, 6, 1, 19, 5, 31, 240280)), (datetime.datetime(2026, 6, 1, 21, 1, 2, 575409), datetime.datetime(2026, 6, 1, 21, 23, 26, 31938)), (datetime.datetime(2026, 6, 1, 23, 18, 59, 878644), datetime.datetime(2026, 6, 1, 23, 41, 20, 641569)), (datetime.datetime(2026, 6, 2, 1, 36, 57, 430085), datetime.datetime(2026, 6, 2, 1, 59, 15, 69079)), (datetime.datetime(2026, 6, 2, 3, 54, 55, 228453), datetime.datetime(2026, 6, 2, 4, 17, 9, 321714)), (datetime.datetime(2026, 6, 2, 6, 12, 53, 277504), datetime.datetime(2026, 6, 2, 6, 35, 3, 402794)), (datetime.datetime(2026, 6, 2, 8, 30, 51, 586448), datetime.datetime(2026, 6, 2, 8, 52, 57, 327156)), (datetime.datetime(2026, 6, 2, 10, 48, 50, 157564), datetime.datetime(2026, 6, 2, 11, 10, 51, 83946)), (datetime.datetime(2026, 6, 2, 13, 6, 48, 987887), datetime.datetime(2026, 6, 2, 13, 28, 44, 693750)), (datetime.datetime(2026, 6, 2, 15, 24, 48, 90342), datetime.datetime(2026, 6, 2, 15, 46, 38, 153940)), (datetime.datetime(2026, 6, 2, 17, 42, 
47, 466301), datetime.datetime(2026, 6, 2, 18, 4, 31, 468815)), (datetime.datetime(2026, 6, 2, 20, 0, 47, 113585), datetime.datetime(2026, 
6, 2, 20, 22, 24, 646340)), (datetime.datetime(2026, 6, 2, 22, 18, 47, 40330), datetime.datetime(2026, 6, 2, 22, 40, 17, 696742)), (datetime.datetime(2026, 6, 3, 0, 36, 47, 249397), datetime.datetime(2026, 6, 3, 0, 58, 10, 613241)), (datetime.datetime(2026, 6, 3, 2, 54, 47, 740273), datetime.datetime(2026, 6, 3, 3, 16, 3, 411772)), (datetime.datetime(2026, 6, 3, 5, 12, 48, 515340), datetime.datetime(2026, 6, 3, 5, 33, 56, 98527)), (datetime.datetime(2026, 6, 3, 7, 30, 49, 580382), datetime.datetime(2026, 6, 3, 7, 51, 48, 673103)), (datetime.datetime(2026, 6, 3, 9, 48, 50, 937221), datetime.datetime(2026, 6, 3, 10, 9, 41, 143911)), (datetime.datetime(2026, 6, 3, 12, 6, 52, 581717), datetime.datetime(2026, 6, 3, 12, 27, 33, 520089)), (datetime.datetime(2026, 6, 3, 14, 24, 54, 523949), datetime.datetime(2026, 6, 3, 14, 45, 25, 801289)), (datetime.datetime(2026, 6, 3, 16, 42, 56, 756663), datetime.datetime(2026, 6, 3, 17, 3, 17, 998800)), (datetime.datetime(2026, 6, 3, 19, 0, 59, 279052), datetime.datetime(2026, 6, 3, 19, 21, 10, 117892)), (datetime.datetime(2026, 6, 3, 21, 19, 2, 103460), datetime.datetime(2026, 6, 3, 21, 39, 2, 166918)), (datetime.datetime(2026, 6, 3, 23, 37, 5, 215318), datetime.datetime(2026, 6, 3, 23, 56, 54, 147831)), (datetime.datetime(2026, 6, 4, 1, 55, 8, 617866), datetime.datetime(2026, 6, 4, 2, 14, 46, 69648)), (datetime.datetime(2026, 6, 4, 4, 13, 12, 315399), datetime.datetime(2026, 6, 4, 4, 32, 37, 942022)), (datetime.datetime(2026, 6, 4, 6, 31, 16, 296860), datetime.datetime(2026, 6, 4, 6, 50, 29, 769002)), (datetime.datetime(2026, 6, 4, 8, 49, 20, 564439), datetime.datetime(2026, 6, 4, 9, 8, 21, 554579)), (datetime.datetime(2026, 6, 4, 11, 7, 25, 120627), datetime.datetime(2026, 6, 4, 11, 26, 13, 319298)), (datetime.datetime(2026, 6, 4, 13, 25, 29, 948185), datetime.datetime(2026, 6, 4, 13, 44, 5, 56387)), (datetime.datetime(2026, 6, 4, 15, 43, 35, 49392), datetime.datetime(2026, 6, 4, 16, 1, 56, 787423)), (datetime.datetime(2026, 6, 4, 18, 1, 40, 420716), datetime.datetime(2026, 6, 4, 18, 19, 48, 508395)), (datetime.datetime(2026, 6, 4, 20, 19, 46, 53618), datetime.datetime(2026, 6, 4, 20, 37, 40, 239107)), (datetime.datetime(2026, 6, 4, 22, 37, 51, 939636), datetime.datetime(2026, 6, 4, 22, 55, 31, 980365)), (datetime.datetime(2026, 6, 5, 0, 55, 58, 69351), datetime.datetime(2026, 6, 5, 1, 13, 23, 752696)), (datetime.datetime(2026, 6, 5, 3, 14, 4, 438227), datetime.datetime(2026, 6, 5, 3, 31, 15, 556040)), (datetime.datetime(2026, 6, 5, 5, 32, 11, 30338), datetime.datetime(2026, 6, 5, 5, 49, 7, 402436)), (datetime.datetime(2026, 6, 5, 7, 50, 17, 836971), datetime.datetime(2026, 6, 5, 8, 6, 59, 312061)), (datetime.datetime(2026, 6, 5, 10, 8, 24, 846114), datetime.datetime(2026, 6, 5, 10, 24, 51, 290462)), (datetime.datetime(2026, 6, 5, 12, 26, 32, 46508), datetime.datetime(2026, 6, 5, 12, 42, 43, 349786)), (datetime.datetime(2026, 6, 5, 
14, 44, 39, 419417), datetime.datetime(2026, 6, 5, 15, 0, 35, 501392)), (datetime.datetime(2026, 6, 5, 17, 2, 46, 943060), datetime.datetime(2026, 6, 5, 17, 18, 27, 764989)), (datetime.datetime(2026, 6, 5, 19, 20, 54, 612978), datetime.datetime(2026, 6, 5, 19, 36, 20, 155188)), (datetime.datetime(2026, 6, 5, 21, 39, 2, 399606), datetime.datetime(2026, 6, 5, 21, 54, 12, 686150)), (datetime.datetime(2026, 6, 5, 23, 
57, 10, 286899), datetime.datetime(2026, 6, 6, 0, 12, 5, 368348)), (datetime.datetime(2026, 6, 6, 2, 15, 18, 246308), datetime.datetime(2026, 6, 6, 2, 29, 58, 231392)), (datetime.datetime(2026, 6, 6, 4, 33, 26, 265264), datetime.datetime(2026, 6, 6, 4, 47, 51, 280497)), (datetime.datetime(2026, 6, 6, 6, 51, 34, 308397), datetime.datetime(2026, 6, 6, 7, 5, 44, 541809)), (datetime.datetime(2026, 6, 6, 9, 9, 42, 353533), datetime.datetime(2026, 6, 6, 9, 23, 38, 37240)), (datetime.datetime(2026, 6, 6, 11, 27, 50, 372443), datetime.datetime(2026, 6, 6, 11, 41, 31, 783867)), (datetime.datetime(2026, 6, 6, 13, 45, 58, 327815), datetime.datetime(2026, 6, 6, 13, 59, 25, 808734)), (datetime.datetime(2026, 6, 6, 16, 4, 6, 198725), datetime.datetime(2026, 6, 6, 16, 17, 20, 126263)), (datetime.datetime(2026, 6, 6, 18, 22, 13, 951775), 
datetime.datetime(2026, 6, 6, 18, 35, 14, 766137)), (datetime.datetime(2026, 6, 6, 20, 40, 21, 544255), datetime.datetime(2026, 6, 6, 20, 53, 9, 748838)), (datetime.datetime(2026, 6, 6, 22, 58, 28, 951953), datetime.datetime(2026, 6, 6, 23, 11, 5, 101799)), (datetime.datetime(2026, 6, 7, 1, 16, 36, 126985), datetime.datetime(2026, 6, 7, 1, 29, 0, 848326)), (datetime.datetime(2026, 6, 7, 3, 34, 43, 47429), datetime.datetime(2026, 6, 7, 3, 46, 57, 12943)), (datetime.datetime(2026, 6, 7, 5, 52, 49, 668657), datetime.datetime(2026, 6, 7, 6, 4, 53, 619795)), (datetime.datetime(2026, 6, 7, 8, 10, 55, 955651), datetime.datetime(2026, 6, 7, 8, 22, 50, 692263)), (datetime.datetime(2026, 6, 7, 10, 37, 28, 80957), datetime.datetime(2026, 6, 7, 10, 49, 21, 856314)), (datetime.datetime(2026, 6, 7, 12, 55, 25, 199843), datetime.datetime(2026, 6, 7, 13, 7, 28, 112887)), (datetime.datetime(2026, 6, 7, 15, 13, 21, 843617), datetime.datetime(2026, 6, 7, 15, 25, 34, 705887)), (datetime.datetime(2026, 6, 7, 17, 31, 18, 50212), datetime.datetime(2026, 6, 7, 17, 43, 41, 602453)), (datetime.datetime(2026, 6, 7, 19, 49, 13, 828843), datetime.datetime(2026, 6, 7, 20, 1, 48, 757684)), (datetime.datetime(2026, 6, 7, 22, 7, 9, 217416), datetime.datetime(2026, 6, 7, 22, 19, 56, 146037)), (datetime.datetime(2026, 6, 8, 0, 25, 4, 230432), datetime.datetime(2026, 6, 8, 0, 38, 3, 725979)), (datetime.datetime(2026, 6, 8, 2, 42, 58, 903719), datetime.datetime(2026, 6, 8, 2, 56, 11, 464167)), (datetime.datetime(2026, 6, 8, 5, 0, 53, 247872), datetime.datetime(2026, 6, 8, 5, 14, 19, 325858)), (datetime.datetime(2026, 6, 8, 7, 18, 47, 291430), datetime.datetime(2026, 6, 8, 7, 32, 27, 282104)), (datetime.datetime(2026, 6, 8, 9, 36, 41, 62268), datetime.datetime(2026, 6, 8, 9, 50, 35, 292999)), (datetime.datetime(2026, 6, 8, 11, 54, 34, 575436), datetime.datetime(2026, 6, 8, 12, 8, 43, 339820)), (datetime.datetime(2026, 6, 8, 14, 12, 27, 860716), datetime.datetime(2026, 6, 8, 14, 26, 51, 386149)), (datetime.datetime(2026, 6, 8, 16, 30, 20, 927800), datetime.datetime(2026, 6, 8, 16, 44, 59, 403705)), (datetime.datetime(2026, 6, 8, 18, 48, 13, 802248), datetime.datetime(2026, 6, 8, 19, 3, 7, 373673)), (datetime.datetime(2026, 
6, 8, 21, 6, 6, 501405), datetime.datetime(2026, 6, 8, 21, 21, 15, 266308)), (datetime.datetime(2026, 6, 8, 23, 23, 59, 42956), datetime.datetime(2026, 6, 8, 23, 39, 23, 64375)), (datetime.datetime(2026, 6, 9, 1, 41, 51, 440757), datetime.datetime(2026, 6, 9, 1, 57, 30, 743222)), (datetime.datetime(2026, 6, 9, 3, 59, 43, 715374), datetime.datetime(2026, 6, 9, 4, 15, 38, 282403)), (datetime.datetime(2026, 6, 9, 6, 
17, 35, 878500), datetime.datetime(2026, 6, 9, 6, 33, 45, 668279)), (datetime.datetime(2026, 6, 9, 8, 35, 27, 943351), datetime.datetime(2026, 6, 9, 8, 51, 52, 883157)), (datetime.datetime(2026, 6, 9, 10, 53, 19, 924430), datetime.datetime(2026, 6, 9, 11, 9, 59, 908518)), (datetime.datetime(2026, 6, 9, 13, 11, 11, 837878), datetime.datetime(2026, 6, 9, 13, 28, 6, 734640)), (datetime.datetime(2026, 6, 9, 15, 29, 3, 686782), datetime.datetime(2026, 6, 9, 15, 46, 13, 350439)), (datetime.datetime(2026, 6, 9, 17, 46, 55, 495612), datetime.datetime(2026, 6, 9, 18, 4, 19, 737701)), (datetime.datetime(2026, 6, 9, 20, 4, 47, 264999), datetime.datetime(2026, 6, 9, 20, 22, 25, 887151)), (datetime.datetime(2026, 6, 9, 22, 22, 39, 7007), datetime.datetime(2026, 6, 9, 22, 40, 31, 795941)), (datetime.datetime(2026, 6, 10, 0, 40, 30, 737253), datetime.datetime(2026, 6, 10, 0, 58, 37, 447091)), (datetime.datetime(2026, 6, 10, 2, 58, 22, 461162), datetime.datetime(2026, 6, 10, 3, 16, 42, 841669)), (datetime.datetime(2026, 6, 10, 5, 16, 14, 184206), datetime.datetime(2026, 6, 10, 5, 34, 47, 968834)), (datetime.datetime(2026, 6, 10, 7, 34, 5, 920154), datetime.datetime(2026, 6, 10, 7, 52, 52, 821927)), (datetime.datetime(2026, 6, 10, 9, 51, 57, 679824), datetime.datetime(2026, 6, 10, 10, 10, 57, 397828)), (datetime.datetime(2026, 6, 10, 12, 9, 49, 463807), datetime.datetime(2026, 6, 10, 
12, 29, 1, 688696)), (datetime.datetime(2026, 6, 10, 14, 27, 41, 283563), datetime.datetime(2026, 6, 10, 14, 47, 5, 698587)), (datetime.datetime(2026, 6, 10, 16, 45, 33, 152247), datetime.datetime(2026, 6, 10, 17, 5, 9, 417737)), (datetime.datetime(2026, 6, 10, 19, 3, 25, 65884), datetime.datetime(2026, 6, 10, 19, 23, 12, 847430)), (datetime.datetime(2026, 6, 10, 21, 21, 17, 39565), datetime.datetime(2026, 6, 10, 
21, 41, 15, 986488)), (datetime.datetime(2026, 6, 10, 23, 39, 9, 78226), datetime.datetime(2026, 6, 10, 23, 59, 18, 832904)), (datetime.datetime(2026, 6, 11, 1, 57, 1, 188907), datetime.datetime(2026, 6, 11, 2, 17, 21, 385274)), (datetime.datetime(2026, 6, 11, 4, 14, 53, 377472), datetime.datetime(2026, 6, 11, 4, 35, 23, 639881)), (datetime.datetime(2026, 6, 11, 6, 32, 45, 650631), datetime.datetime(2026, 6, 11, 6, 53, 25, 609691)), (datetime.datetime(2026, 6, 11, 8, 50, 38, 11488), datetime.datetime(2026, 6, 11, 9, 11, 27, 281009)), (datetime.datetime(2026, 6, 11, 11, 8, 30, 471317), datetime.datetime(2026, 6, 11, 11, 29, 28, 663373)), (datetime.datetime(2026, 6, 11, 13, 26, 23, 34992), datetime.datetime(2026, 6, 11, 13, 47, 29, 751820)), (datetime.datetime(2026, 6, 11, 15, 44, 15, 707335), datetime.datetime(2026, 6, 11, 
16, 5, 30, 555174)), (datetime.datetime(2026, 6, 11, 18, 2, 8, 493230), datetime.datetime(2026, 6, 11, 18, 23, 31, 71852)), (datetime.datetime(2026, 6, 11, 20, 20, 1, 399424), datetime.datetime(2026, 6, 11, 20, 41, 31, 304474)), (datetime.datetime(2026, 6, 11, 22, 37, 54, 434295), datetime.datetime(2026, 6, 11, 22, 59, 31, 257514)), (datetime.datetime(2026, 6, 12, 0, 55, 47, 597102), datetime.datetime(2026, 6, 12, 1, 17, 30, 930595)), (datetime.datetime(2026, 6, 12, 3, 13, 40, 895475), datetime.datetime(2026, 6, 12, 3, 35, 30, 331381)), (datetime.datetime(2026, 6, 12, 5, 31, 34, 338890), datetime.datetime(2026, 6, 12, 5, 53, 29, 457566)), (datetime.datetime(2026, 6, 12, 7, 49, 27, 931079), datetime.datetime(2026, 6, 12, 8, 11, 28, 315761)), (datetime.datetime(2026, 6, 12, 10, 7, 21, 672698), datetime.datetime(2026, 6, 12, 
10, 29, 26, 913163)), (datetime.datetime(2026, 6, 12, 12, 25, 15, 575281), datetime.datetime(2026, 6, 12, 12, 47, 25, 242532)), (datetime.datetime(2026, 6, 12, 14, 43, 9, 638762), datetime.datetime(2026, 6, 12, 15, 5, 23, 317404)), (datetime.datetime(2026, 6, 12, 17, 1, 3, 874115), datetime.datetime(2026, 6, 12, 17, 23, 21, 141774)), (datetime.datetime(2026, 6, 12, 19, 18, 58, 279219), datetime.datetime(2026, 6, 12, 19, 41, 18, 718563)), (datetime.datetime(2026, 6, 12, 21, 36, 52, 868529), datetime.datetime(2026, 6, 12, 21, 59, 16, 47749)), (datetime.datetime(2026, 6, 12, 23, 54, 47, 635094), datetime.datetime(2026, 6, 13, 0, 17, 13, 134017)), (datetime.datetime(2026, 6, 13, 2, 12, 42, 
594351), datetime.datetime(2026, 6, 13, 2, 35, 9, 988231)), (datetime.datetime(2026, 6, 13, 4, 30, 37, 748622), datetime.datetime(2026, 6, 
13, 4, 53, 6, 607780)), (datetime.datetime(2026, 6, 13, 6, 48, 33, 103251), datetime.datetime(2026, 6, 13, 7, 11, 3, 4133)), (datetime.datetime(2026, 6, 13, 9, 6, 28, 659428), datetime.datetime(2026, 6, 13, 9, 28, 59, 179345)), (datetime.datetime(2026, 6, 13, 11, 24, 24, 422087), datetime.datetime(2026, 6, 13, 11, 46, 55, 132404)), (datetime.datetime(2026, 6, 13, 13, 42, 20, 400952), datetime.datetime(2026, 6, 13, 14, 4, 50, 877077)), (datetime.datetime(2026, 6, 13, 16, 0, 16, 596201), datetime.datetime(2026, 6, 13, 16, 22, 46, 410927)), (datetime.datetime(2026, 6, 13, 18, 18, 13, 12219), datetime.datetime(2026, 6, 13, 18, 40, 41, 745180)), (datetime.datetime(2026, 6, 13, 20, 36, 9, 660518), datetime.datetime(2026, 6, 13, 20, 58, 36, 882199)), (datetime.datetime(2026, 6, 13, 22, 54, 6, 538758), datetime.datetime(2026, 6, 13, 23, 16, 31, 824358)), (datetime.datetime(2026, 6, 14, 1, 12, 3, 653593), datetime.datetime(2026, 6, 14, 1, 34, 26, 575954)), (datetime.datetime(2026, 6, 14, 3, 30, 1, 7206), datetime.datetime(2026, 6, 14, 3, 52, 21, 145739)), (datetime.datetime(2026, 6, 14, 5, 41, 3, 459429), datetime.datetime(2026, 6, 14, 6, 3, 21, 56220)), (datetime.datetime(2026, 6, 14, 7, 58, 57, 884710), datetime.datetime(2026, 6, 14, 8, 21, 18, 607000)), (datetime.datetime(2026, 6, 14, 10, 16, 52, 489819), datetime.datetime(2026, 6, 14, 10, 39, 15, 912792)), (datetime.datetime(2026, 6, 14, 12, 34, 47, 280813), datetime.datetime(2026, 6, 14, 12, 57, 12, 978367)), (datetime.datetime(2026, 6, 14, 14, 52, 42, 258039), datetime.datetime(2026, 6, 14, 15, 15, 9, 810530)), (datetime.datetime(2026, 6, 14, 17, 10, 37, 428844), datetime.datetime(2026, 6, 14, 17, 33, 6, 408794)), (datetime.datetime(2026, 6, 14, 19, 28, 32, 801270), datetime.datetime(2026, 6, 14, 19, 51, 2, 783200)), (datetime.datetime(2026, 6, 14, 21, 46, 28, 379969), datetime.datetime(2026, 6, 14, 22, 8, 58, 935733)), (datetime.datetime(2026, 6, 15, 0, 4, 24, 167720), datetime.datetime(2026, 6, 15, 0, 26, 54, 874902)), (datetime.datetime(2026, 6, 15, 2, 22, 20, 165418), datetime.datetime(2026, 6, 15, 2, 44, 50, 596471)), (datetime.datetime(2026, 6, 15, 4, 40, 16, 385202), datetime.datetime(2026, 6, 15, 5, 2, 46, 115465)), (datetime.datetime(2026, 6, 15, 6, 58, 12, 825241), datetime.datetime(2026, 6, 15, 7, 20, 41, 427735)), (datetime.datetime(2026, 6, 15, 9, 16, 9, 491868), datetime.datetime(2026, 6, 15, 9, 38, 36, 546611)), (datetime.datetime(2026, 6, 15, 11, 34, 6, 394153), datetime.datetime(2026, 6, 15, 11, 56, 31, 471475)), (datetime.datetime(2026, 6, 15, 13, 52, 3, 532887), datetime.datetime(2026, 6, 15, 14, 14, 26, 207611)), (datetime.datetime(2026, 6, 15, 16, 10, 0, 910872), datetime.datetime(2026, 6, 15, 16, 32, 20, 765415)), (datetime.datetime(2026, 6, 15, 18, 27, 58, 537382), datetime.datetime(2026, 6, 15, 18, 50, 15, 145039)), (datetime.datetime(2026, 6, 15, 20, 45, 56, 412821), datetime.datetime(2026, 6, 15, 21, 8, 9, 350599)), (datetime.datetime(2026, 6, 15, 23, 3, 54, 539966), datetime.datetime(2026, 6, 15, 23, 26, 3, 393937)), (datetime.datetime(2026, 6, 16, 1, 21, 52, 925189), datetime.datetime(2026, 6, 16, 1, 43, 57, 270985)), (datetime.datetime(2026, 6, 16, 3, 39, 51, 573144), datetime.datetime(2026, 6, 16, 4, 1, 50, 995125)), (datetime.datetime(2026, 6, 16, 5, 57, 50, 486960), datetime.datetime(2026, 6, 16, 
6, 19, 44, 563571)), (datetime.datetime(2026, 6, 16, 8, 15, 49, 669414), datetime.datetime(2026, 6, 16, 8, 37, 37, 990973)), (datetime.datetime(2026, 6, 16, 10, 33, 49, 118774), datetime.datetime(2026, 6, 16, 10, 55, 31, 276588)), (datetime.datetime(2026, 6, 16, 12, 51, 48, 846954), datetime.datetime(2026, 6, 16, 13, 13, 24, 428044)), (datetime.datetime(2026, 6, 16, 15, 9, 48, 853197), datetime.datetime(2026, 6, 16, 15, 31, 17, 449736)), (datetime.datetime(2026, 6, 16, 17, 27, 49, 140078), datetime.datetime(2026, 6, 16, 17, 49, 10, 351190)), (datetime.datetime(2026, 6, 16, 19, 45, 49, 712591), datetime.datetime(2026, 6, 16, 20, 7, 3, 129711)), (datetime.datetime(2026, 6, 16, 22, 3, 50, 
567971), datetime.datetime(2026, 6, 16, 22, 24, 55, 799341)), (datetime.datetime(2026, 6, 17, 0, 21, 51, 709525), datetime.datetime(2026, 6, 17, 0, 42, 48, 360933)), (datetime.datetime(2026, 6, 17, 2, 39, 53, 144432), datetime.datetime(2026, 6, 17, 3, 0, 40, 823506)), (datetime.datetime(2026, 6, 17, 4, 57, 54, 863638), datetime.datetime(2026, 6, 17, 5, 18, 33, 194592)), (datetime.datetime(2026, 6, 17, 7, 15, 56, 881701), datetime.datetime(2026, 6, 17, 7, 36, 25, 475803)), (datetime.datetime(2026, 6, 17, 9, 33, 59, 187153), datetime.datetime(2026, 6, 
17, 9, 54, 17, 671916)), (datetime.datetime(2026, 6, 17, 11, 52, 1, 784475), datetime.datetime(2026, 6, 17, 12, 12, 9, 799021)), (datetime.datetime(2026, 6, 17, 14, 10, 4, 673784), datetime.datetime(2026, 6, 17, 14, 30, 1, 855224)), (datetime.datetime(2026, 6, 17, 16, 28, 7, 853934), datetime.datetime(2026, 6, 17, 16, 47, 53, 848606)), (datetime.datetime(2026, 6, 17, 18, 46, 11, 323017), datetime.datetime(2026, 6, 17, 19, 5, 45, 786070)), (datetime.datetime(2026, 6, 17, 21, 4, 15, 80568), datetime.datetime(2026, 6, 17, 21, 23, 37, 679982)), (datetime.datetime(2026, 6, 17, 23, 22, 19, 120866), datetime.datetime(2026, 6, 17, 23, 41, 29, 531966)), (datetime.datetime(2026, 6, 18, 1, 40, 23, 447579), datetime.datetime(2026, 6, 18, 1, 59, 21, 351694)), (datetime.datetime(2026, 6, 18, 3, 58, 28, 50856), datetime.datetime(2026, 6, 18, 4, 17, 13, 145231)), (datetime.datetime(2026, 6, 18, 6, 16, 32, 925082), datetime.datetime(2026, 6, 18, 6, 35, 4, 925064)), (datetime.datetime(2026, 6, 18, 8, 34, 38, 71466), datetime.datetime(2026, 6, 18, 8, 52, 56, 695607)), (datetime.datetime(2026, 6, 18, 10, 52, 43, 479985), datetime.datetime(2026, 6, 18, 11, 10, 48, 465365)), (datetime.datetime(2026, 6, 18, 13, 10, 49, 148011), datetime.datetime(2026, 6, 18, 13, 28, 40, 246711)), (datetime.datetime(2026, 6, 18, 15, 28, 55, 57679), datetime.datetime(2026, 6, 18, 15, 46, 32, 52840)), (datetime.datetime(2026, 6, 18, 17, 47, 1, 213235), datetime.datetime(2026, 6, 18, 18, 4, 23, 882362)), (datetime.datetime(2026, 6, 18, 20, 5, 7, 592366), datetime.datetime(2026, 6, 18, 20, 22, 15, 756530)), (datetime.datetime(2026, 6, 18, 22, 23, 14, 196764), datetime.datetime(2026, 6, 18, 22, 40, 7, 681827)), (datetime.datetime(2026, 6, 19, 0, 41, 21, 3690), datetime.datetime(2026, 6, 19, 0, 57, 59, 673444)), (datetime.datetime(2026, 6, 19, 2, 59, 28, 4392), datetime.datetime(2026, 6, 19, 3, 15, 51, 740282)), (datetime.datetime(2026, 6, 19, 5, 17, 35, 189221), datetime.datetime(2026, 6, 19, 5, 33, 43, 896844)), (datetime.datetime(2026, 6, 19, 7, 35, 42, 536542), datetime.datetime(2026, 6, 19, 7, 51, 36, 153416)), (datetime.datetime(2026, 6, 19, 9, 53, 50, 29349), datetime.datetime(2026, 6, 19, 10, 9, 28, 525846)), (datetime.datetime(2026, 6, 19, 12, 11, 57, 652297), datetime.datetime(2026, 6, 19, 12, 27, 21, 33898)), (datetime.datetime(2026, 6, 19, 14, 30, 5, 383627), datetime.datetime(2026, 6, 19, 14, 45, 13, 686992)), (datetime.datetime(2026, 6, 19, 16, 48, 13, 203326), datetime.datetime(2026, 6, 19, 17, 3, 6, 508777)), (datetime.datetime(2026, 6, 19, 19, 6, 21, 90045), datetime.datetime(2026, 6, 19, 19, 20, 59, 507491)), (datetime.datetime(2026, 6, 19, 21, 24, 29, 15132), datetime.datetime(2026, 6, 19, 21, 38, 52, 708852)), (datetime.datetime(2026, 6, 19, 23, 42, 36, 955891), datetime.datetime(2026, 6, 19, 23, 56, 46, 133624)), (datetime.datetime(2026, 6, 20, 2, 0, 44, 888106), datetime.datetime(2026, 6, 20, 2, 14, 39, 797312)), (datetime.datetime(2026, 6, 20, 4, 18, 52, 777511), datetime.datetime(2026, 6, 20, 4, 32, 33, 719579)), (datetime.datetime(2026, 6, 20, 6, 37, 0, 597180), datetime.datetime(2026, 6, 20, 6, 50, 27, 927324)), (datetime.datetime(2026, 6, 20, 8, 55, 8, 314296), datetime.datetime(2026, 6, 20, 9, 8, 22, 440198)), (datetime.datetime(2026, 6, 20, 11, 13, 15, 896735), datetime.datetime(2026, 6, 20, 11, 26, 17, 284022)), (datetime.datetime(2026, 6, 20, 13, 31, 23, 310819), datetime.datetime(2026, 6, 20, 13, 44, 12, 476254)), (datetime.datetime(2026, 6, 20, 15, 49, 30, 522048), datetime.datetime(2026, 6, 20, 16, 2, 8, 49016)), (datetime.datetime(2026, 6, 20, 18, 7, 37, 495353), datetime.datetime(2026, 6, 20, 18, 20, 4, 23185)), (datetime.datetime(2026, 6, 20, 20, 25, 44, 195449), datetime.datetime(2026, 6, 20, 
20, 38, 0, 418995)), (datetime.datetime(2026, 6, 20, 22, 43, 50, 586870), datetime.datetime(2026, 6, 20, 22, 55, 57, 264116)), (datetime.datetime(2026, 6, 21, 1, 1, 56, 634246), datetime.datetime(2026, 6, 21, 1, 13, 54, 579185)), (datetime.datetime(2026, 6, 21, 3, 28, 24, 972039), datetime.datetime(2026, 6, 21, 3, 40, 28, 749752)), (datetime.datetime(2026, 6, 21, 5, 46, 21, 935843), datetime.datetime(2026, 6, 21, 
5, 58, 35, 60583)), (datetime.datetime(2026, 6, 21, 8, 4, 18, 443685), datetime.datetime(2026, 6, 21, 8, 16, 41, 689565)), (datetime.datetime(2026, 6, 21, 10, 22, 14, 523380), datetime.datetime(2026, 6, 21, 10, 34, 48, 601510)), (datetime.datetime(2026, 6, 21, 12, 40, 10, 198983), datetime.datetime(2026, 6, 21, 12, 52, 55, 762142)), (datetime.datetime(2026, 6, 21, 14, 58, 5, 485096), datetime.datetime(2026, 6, 21, 15, 11, 3, 134001)), (datetime.datetime(2026, 6, 21, 17, 16, 0, 415377), datetime.datetime(2026, 6, 21, 17, 29, 10, 681362)), (datetime.datetime(2026, 6, 21, 19, 33, 55, 13226), datetime.datetime(2026, 6, 21, 19, 47, 18, 376590)), (datetime.datetime(2026, 6, 21, 21, 51, 49, 296454), datetime.datetime(2026, 6, 21, 22, 5, 26, 181806)), (datetime.datetime(2026, 6, 22, 0, 9, 43, 290006), datetime.datetime(2026, 6, 22, 0, 23, 34, 64520)), (datetime.datetime(2026, 6, 22, 2, 27, 37, 15663), datetime.datetime(2026, 6, 22, 2, 41, 41, 994288)), (datetime.datetime(2026, 6, 22, 4, 45, 30, 497017), datetime.datetime(2026, 6, 22, 4, 59, 49, 943916)), (datetime.datetime(2026, 6, 22, 7, 3, 23, 750401), datetime.datetime(2026, 6, 22, 7, 17, 57, 888703)), (datetime.datetime(2026, 6, 22, 9, 21, 16, 803035), datetime.datetime(2026, 6, 22, 9, 36, 5, 794324)), (datetime.datetime(2026, 6, 22, 11, 39, 9, 666331), datetime.datetime(2026, 6, 22, 11, 54, 13, 644454)), (datetime.datetime(2026, 6, 22, 13, 57, 2, 359135), datetime.datetime(2026, 6, 22, 14, 12, 21, 408827)), (datetime.datetime(2026, 6, 22, 16, 14, 54, 901713), datetime.datetime(2026, 6, 22, 16, 30, 29, 71757)), (datetime.datetime(2026, 6, 22, 18, 32, 47, 307868), datetime.datetime(2026, 6, 22, 
18, 48, 36, 609432)), (datetime.datetime(2026, 6, 22, 20, 50, 39, 594619), datetime.datetime(2026, 6, 22, 21, 6, 44, 4545)), (datetime.datetime(2026, 6, 22, 23, 8, 31, 772161), datetime.datetime(2026, 6, 22, 23, 24, 51, 240568)), (datetime.datetime(2026, 6, 23, 1, 26, 23, 858732), datetime.datetime(2026, 6, 23, 1, 42, 58, 302965)), (datetime.datetime(2026, 6, 23, 3, 44, 15, 866563), datetime.datetime(2026, 6, 23, 
4, 1, 5, 171688)), (datetime.datetime(2026, 6, 23, 6, 2, 7, 808099), datetime.datetime(2026, 6, 23, 6, 19, 11, 837022)), (datetime.datetime(2026, 6, 23, 8, 19, 59, 695309), datetime.datetime(2026, 6, 23, 8, 37, 18, 286186)), (datetime.datetime(2026, 6, 23, 10, 37, 51, 536802), 
datetime.datetime(2026, 6, 23, 10, 55, 24, 509860)), (datetime.datetime(2026, 6, 23, 12, 55, 43, 346831), datetime.datetime(2026, 6, 23, 13, 13, 30, 494881)), (datetime.datetime(2026, 6, 23, 15, 13, 35, 130958), datetime.datetime(2026, 6, 23, 15, 31, 36, 237802)), (datetime.datetime(2026, 6, 23, 17, 31, 26, 907377), datetime.datetime(2026, 6, 23, 17, 49, 41, 722567)), (datetime.datetime(2026, 6, 23, 19, 49, 18, 680563), datetime.datetime(2026, 6, 23, 20, 7, 46, 948879)), (datetime.datetime(2026, 6, 23, 22, 7, 10, 454972), datetime.datetime(2026, 6, 23, 22, 25, 51, 904103)), (datetime.datetime(2026, 6, 24, 0, 25, 2, 243232), datetime.datetime(2026, 6, 24, 0, 43, 56, 587148)), (datetime.datetime(2026, 6, 24, 2, 42, 54, 58935), datetime.datetime(2026, 6, 24, 3, 2, 0, 996904)), (datetime.datetime(2026, 6, 24, 5, 0, 45, 903572), datetime.datetime(2026, 6, 24, 5, 20, 5, 120314)), (datetime.datetime(2026, 6, 24, 7, 18, 37, 783604), datetime.datetime(2026, 6, 24, 7, 
38, 8, 964459)), (datetime.datetime(2026, 6, 24, 9, 36, 29, 710554), datetime.datetime(2026, 6, 24, 9, 56, 12, 519760)), (datetime.datetime(2026, 6, 24, 11, 54, 21, 693843), datetime.datetime(2026, 6, 24, 12, 14, 15, 785223)), (datetime.datetime(2026, 6, 24, 14, 12, 13, 732378), datetime.datetime(2026, 6, 24, 14, 32, 18, 759947)), (datetime.datetime(2026, 6, 24, 16, 30, 5, 840336), datetime.datetime(2026, 6, 24, 16, 50, 21, 441891)), (datetime.datetime(2026, 6, 24, 18, 47, 58, 24336), datetime.datetime(2026, 6, 24, 19, 8, 23, 833051)), (datetime.datetime(2026, 6, 24, 21, 5, 50, 285454), datetime.datetime(2026, 6, 24, 21, 26, 25, 935327)), (datetime.datetime(2026, 6, 24, 23, 23, 42, 629928), datetime.datetime(2026, 6, 24, 23, 44, 27, 742414)), (datetime.datetime(2026, 6, 25, 1, 41, 35, 73647), datetime.datetime(2026, 6, 25, 2, 1))]


print(has_coinciding_intervals(access_A))

print(datetime.datetime(2026, 6, 24, 9, 56, 12, 519760) - datetime.datetime(2026, 6, 24, 9, 36, 29, 710554))