# WHY DID WE USED USE DJANGO.CORS.HEADERS NOT IN THIS API BUT WHEN YOU WILL TRY TO CONNECT THIS API WITH THE FRONTEND LIKE REACT OT SOMETHING ELSE IT WILL GIVE AN COMMON CORS POLICY ERROR THAT ERROR DOES NOT OCCUR SO WE ARE SOLVING IT USING  THE  DJANGO CORS HEADERS AND DOWNOLAING IT INTSALL IT THE APP SETTINGGS  AND IN THE MIDDLEWARE   AND THEN WRITNG THIS IN THE SETTING CORS_ALLOWED_ORIGINS = [
  
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]   THIS FOR THE PROJECT DEPLOYMENT SO here we are using local host

# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________
                                       # {MODELS }
    
# IN THE MODELS WE ARE NOT USING THE DEFAULT USER MODEL PROVIDED BY THE DJANGO AS IS USES THE USERNAME TO LOGIN THE USER BUT WE WILL USE THE EAMIL TO LOGIN USER AND WE ALSO REQUIRE MORE FIELD SO WE WIL.. 


# email=self.normalize_email(email),    
# HERE WHY DO WE NEED THE EMAIL TO BE LOWERCASED BEACUSE  :

# normalize_email converts email addresses to lowercase and removes extra spaces. This ensures consistency because email addresses are case-insensitive (e.g., User@Example.com is the same as user@example.com). Most email providers, like Gmail and Yahoo, treat the local part of the email as case-insensitive. It prevents issues like duplicate accounts and mismatches during comparisons by storing and handling emails in a uniform format.

        

