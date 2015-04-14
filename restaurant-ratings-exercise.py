

def restaurant_ratings(filepath):

    """ This will tokenize the file and split by colons creating an array"""

    for line in open(filepath):
        restaurant_scores = line.rstrip().split(':')
        
        #print restaurant_scores

    """ Creates a dictionary from array. """ 
                        
    restaurant_dict = {i: restaurant_ratings for i in restaurant_scores}          
    name = restaurant_scores[0]  
    rating = restaurant_scores[1]
   
    restaurant_dict[name] = rating 
    
    #print name
    #print rating 

    for name, rating in restaurant_scores:
        print "Restaurant %s is rated at %s" % name, rating

restaurant_ratings ('scores.txt')
