-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.id, c.name
FROM cities as c
WHERE c.states_id = 
    (
        SELECT st.id
        FROM states as st
        WHERE st.name = "California"
    )
ORDER BY c.id;
