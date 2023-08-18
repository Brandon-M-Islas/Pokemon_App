SELECT secondary_val, primary_val
FROM secondary
JOIN prime ON secondary.primary_id = prime.primary_id;
