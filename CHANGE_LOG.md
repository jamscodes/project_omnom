<h1>Change Log</h1>
<p>This document is a place that will provide more details for each major/minor update that is made to this project.</p>
<p>Updates will be numbered and will be sorted in descending order (the most recent update will be at the top of this file, etc.)</p>
<hr>
<h2>Update #2</h2>
<h3>Models:</h3>
<ul>
    <li>The Food model has a static method to determine caloric density</li>
    <li>All queries in the Food model have been updated accordingly</li>
    <li>The Meal model has a get_all_meals class method that returns all meals from the database</li>
    <li>The Meal model’s __init__ method now includes setting an id for the object</li>
</ul>
<h3>Views:</h3>
<ul>
    <li>Updated forms to send calories and serving size in a number field</li>
    <li>Edited navbar to include a logout button and change the “active” state of nav links appropriately</li>
    <li>Added a “meals” table to the /dashboard/ view</li>
</ul>
<h3>Controllers:</h3>
<ul>
    <li>Updated form handlers to convert fields to use the appropriate data types for values</li>
</ul>

<hr>

<h2>Update #1</h2>
<p>Initialization of project, etc.</p>