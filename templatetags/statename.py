from django import template
register = template.Library()

@register.filter(name='state_name')
def state_name(value):
    
    if value == "AL":
        return "Alabama"
    elif value == "AK":
        return "Alaska"
    elif value == "AZ":
        return "Arizona"
    elif value == "AR":
        return "Arkansas"
    elif value == "CA":
        return "California"
    elif value == "CO":
        return "Colorado"
    elif value == "CT":
        return "Connecticut"
    elif value == "DE":
        return "Delaware"
    elif value == "FL":
        return "Florida"
    elif value == "GA":
        return "Georgia"
    elif value == "HI":
        return "Hawaii"
    elif value == "ID":
        return "Idaho"
    elif value == "IL":
        return "Illinois"
    elif value == "IN":
        return "Indiana"
    elif value == "IA":
        return "Iowa"
    elif value == "KS":
        return "Kansas"
    elif value == "KY":
        return "Kentucky"
    elif value == "LA":
        return "Louisiana"
    elif value == "ME":
        return "Maine"
    elif value == "MD":
        return "Maryland"
    elif value == "MA":
        return "Massachusetts"
    elif value == "MI":
        return "Michigan"
    elif value == "MN":
        return "Minnesota"
    elif value == "MS":
        return "Mississippi"
    elif value == "MO":
        return "Missouri"
    elif value == "MT":
        return "Montana"
    elif value == "NE":
        return "Nebraska"
    elif value == "NV":
        return "Nevada"
    elif value == "NH":
        return "New Hampshire"
    elif value == "NJ":
        return "New Jersey"
    elif value == "NM":
        return "New Mexico"
    elif value == "NY":
        return "New York"
    elif value == "NC":
        return "North Carolina"
    elif value == "ND":
        return "North Dakota"
    elif value == "OH":
        return "Ohio"
    elif value == "OK":
        return "Oklahoma"
    elif value == "OR":
        return "Oregon"
    elif value == "PA":
        return "Pennsylvania"
    elif value == "RI":
        return "Rhode Island"
    elif value == "SC":
        return "South Carolina"
    elif value == "SD":
        return "South Dakota"
    elif value == "TN":
        return "Tennessee"
    elif value == "TX":
        return "Texas"
    elif value == "UT":
        return "Utah"
    elif value == "VT":
        return "Vermont"
    elif value == "VA":
        return "Virginia"
    elif value == "WA":
        return "Washington"
    elif value == "WI":
        return "Wisconsin"
    elif value == "WV":
        return "West Virginia"
    elif value == "WY":
        return "Wyoming"
    
    else:
        return value