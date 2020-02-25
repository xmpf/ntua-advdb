# Advanced Databases
Advanced Topics in Database Systems (atds) - 9th Semester  
Michalis Papadopoullos (03114702)  

## Γενικές Πληροφορίες

## Σχετικά με την εργασία
Machine Learning - Ομαδοποίηση δεδομένων με εκτέλεση του k-means αλγόριθμου
Χρησιμοποιώντας τα δεδομένα που περιγράψαμε, στο τρίτο θέμα θέλουμε να βρούμε τις κεντρικές συντεταγμένες των top 5 περιοχών επιβίβασης πελατών.
Για το σκοπό αυτό ζητείται να υλοποιηθεί ο αλγόριθμος ομαδοποίησης [k-means](https://en.wikipedia.org/wiki/K-means_clustering​), τον οποίο θα χρησιμοποιήσουμε για να ομαδοποιήσουμε τα σημεία επιβίβασης σε k=5 περιοχές (clusters) και να βρούμε το κέντρο των σημείων κάθε περιοχής.

Note: https://en.wikipedia.org/wiki/Null_Island)  

### Παραδοτέα
Η παράδοση θα αποτελείται από:
○ Μια σύντομη αναφορά όπου θα περιγράφετε την μεθοδολογία που ακολουθήσατε (όχι κώδικας εδώ).
○ Ψευδοκώδικας για τα προγράμματα Map/Reduce που χρησιμοποιήσατε για κάθε κομμάτι της άσκησης. Ο ψευδοκώδικας θα δείχνει εποπτικά τα key/values που παίρνει η συνάρτηση map, την επεξεργασία που τους κάνει, τα key/values που κάνει emit στην συνάρτηση reduce, και την επεξεργασία που κάνει η reduce (σαν τον ψευδοκώδικα του wordcount).
○ Link στο hdfs site όπου έχετε βάλει τα datasets.
○ Ένα zip file με τον κώδικα.
○ Ένα zip file με τα τελικά αποτελέσματα.
○ Ένα zip file με τα log-files των εργασιών MapReduce από τις οποίες βγήκαν τα αποτελέσματα