#@api @filters
Feature: Filter on dates
  As a stock broker
  I need to filter stocks on date intervals
  In order to research only relevant data and speed up my work

  Scenario Outline: Valid from-to dates
    Given <date_from> and <date_to> provided as query parameters
      When observing filtered data
      Then results display
      And there are no records before <date_from>
      And there are no records after <date_to>

    Examples: Dates
      | date_from          | date_to    |
      | 2019-05-11         | 2019-06-09 |

  Scenario Outline: Invalid date_from and invalid date_to
    Given <date_from> and <date_to> provided as invalid query parameters
      When observing results
      Then no results display

    Examples: Dates
      | date_from   | date_to    |
      | abc         | 123        |

  Scenario Outline: Only date_from provided
    Given only <date_from> provided as query parameter
      When observing results filtered based on <date_from>
      Then no results before <date_from> display
      And only results to maximum available date display

    Examples: Dates
      | date_from   | date_to    |
      | 2019-05-10  |            |

  Scenario Outline: Only date_to provided
    Given <date_to> is the only query parameter
      When observing results for <date_to>
      Then no results after <date_to> display
      And only results from earliest available date display

    Examples: Dates
      | date_from  | date_to      |
      |            | 2019-07-21  |
