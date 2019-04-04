Feature: testing typing text

Scenario: visit google start page and type
  When I have opened google starting page
  Then I have written text to the textbox
  Then I click on the 'pizzalviv.com' link
  Then I click on the 'Піца' button
  Then I click 'next' button until find the 'pepperoni' pizza
  Then I click on the 'Pepperoni' pizza
  Then I click on the 'add to the basket' button
  Then I click on the 'my orders' button
  Then I click on the 'remove order' button
