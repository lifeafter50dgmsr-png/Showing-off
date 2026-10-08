# velvet_dice_repo.py
# Velvet Dice Game Repository
# Consent is always 100%. Pass is always available.

game = {
    "name": "Velvet Dice",
    "core_rules": {
        "consent": "100% — anyone can pass any card, action, or intensity at any time",
        "pass_option": True,
        "dice_purpose": [
            "Randomize Action + Body / Sensation",
            "Control intensity level",
            "Keep power balanced between players"
        ]
    },

    "heat_ladder": [
        "Mild",
        "Hot",
        "Spicy",
        "Burned Your Tongue",
        "Tastes Like a Dill"
    ],

    "keepers": {
        "green_keeper": {
            "color": "Electric Teal",
            "deck": "Burned Your Tongue",
            "energy": "Controlled heat, temperature contrast, sustained sensation"
        },
        "purple_keeper": {
            "color": "Neon Purple",
            "deck": "Tastes Like a Dill",
            "energy": "Layered, consuming, multi-sensation play"
        }
    },

    "card_back": {
        "style": "Side-by-side",
        "left": "Electric Teal (smiling)",
        "right": "Neon Purple (serious)",
        "applies_to": ["Burned Your Tongue", "Tastes Like a Dill"]
    },

    "allowed_tools": [
        "Ice",
        "Water",
        "Safe wax / candling",
        "Pinching",
        "Licking",
        "Spanking",
        "Temperature contrast"
    ],

    "decks": {
        "Burned_Your_Tongue": {
            "position": "After Spicy",
            "keeper": "Green Keeper",
            "focus": "Heat, contrast, sustained tongue work, impact + temperature",
            "cards": [
                {"id": 1, "text": "Ice then tongue on one spot.", "options": ["Pass", "Keep going", "Switch who gives/receives"]},
                {"id": 2, "text": "One firm spank, then lick the heat.", "options": ["Pass", "Add a second spank", "Soften it"]},
                {"id": 3, "text": "Pinch a short line, then soothe with tongue.", "options": ["Pass", "Longer line", "Switch roles"]},
                {"id": 4, "text": "Ice held in mouth, pressed and dragged.", "options": ["Pass", "Add light pinching around it", "Stop after 10 seconds"]},
                {"id": 5, "text": "Controlled safe wax drip, immediately followed by tongue.", "options": ["Pass", "Skip wax, use only ice + tongue", "Double the contrast"]},
                {"id": 6, "text": "Spank once, ice the sting, then warm with mouth.", "options": ["Pass", "Skip ice", "Extra spank first"]},
                {"id": 7, "text": "Trace ice, follow with flat tongue strokes.", "options": ["Pass", "Reverse the order", "Choose the path together"]},
                {"id": 8, "text": "Pinch and hold while tongue works elsewhere.", "options": ["Pass", "Release early", "Add a second pinch point"]},
                {"id": 9, "text": "Ice on inner thigh, tongue right behind it.", "options": ["Pass", "Stay lower", "Move higher only if both agree"]},
                {"id": 10, "text": "Light pinches + licking in alternating rhythm.", "options": ["Pass", "Faster", "Slower", "Switch who leads"]},
                {"id": 11, "text": "Safe wax trail, cool with water or ice, then tongue.", "options": ["Pass", "Skip wax", "Use only temperature contrast"]},
                {"id": 12, "text": "Spank, pause, lick, repeat once.", "options": ["Pass", "One round only", "Add a third if both want"]},
                {"id": 13, "text": "Ice circle, then tongue fills the circle.", "options": ["Pass", "Smaller circle", "Larger area"]},
                {"id": 14, "text": "Pinch a path, then lick back over every mark.", "options": ["Pass", "Softer pinches", "Skip pinching, tongue only"]},
                {"id": 15, "text": "Layer: ice → light spank → tongue.", "options": ["Pass", "Drop one layer", "Change the order"]},
                {"id": 16, "text": "Ice in mouth + slow drag, then pure tongue heat.", "options": ["Pass", "Keep the ice longer", "Switch immediately to tongue"]},
                {"id": 17, "text": "Controlled wax (safe), soothe with ice, claim with tongue.", "options": ["Pass", "No wax", "Ice + tongue only"]},
                {"id": 18, "text": "Spank for warmth, then taste every bit of the heat.", "options": ["Pass", "Lighter spanks", "Stop at warmth, no tongue"]},
                {"id": 19, "text": "Pinch + ice at the same time, tongue finishes.", "options": ["Pass", "Separate the sensations", "Choose intensity together"]},
                {"id": 20, "text": "Final: ice + spank + tongue until one of you calls stop.", "options": ["Pass", "Choose only two of the three", "End sooner"]}
            ]
        },

        "Tastes_Like_a_Dill": {
            "position": "After Burned Your Tongue",
            "keeper": "Purple Keeper",
            "focus": "Layered sensations, deeper immersion, multiple tools at once",
            "cards": [
                {"id": 1, "text": "Full layer: ice → safe wax → tongue.", "options": ["Pass", "Drop wax", "Drop ice", "Both decide order"]},
                {"id": 2, "text": "Spank for heat, then long tongue strokes over it.", "options": ["Pass", "Lighter impact", "Tongue only"]},
                {"id": 3, "text": "Ice held between lips and dragged, pinching the edges.", "options": ["Pass", "No pinching", "Shorter drag"]},
                {"id": 4, "text": "Safe wax trail, cool with water/ice, tongue claims it.", "options": ["Pass", "Skip wax", "Use only cool + tongue"]},
                {"id": 5, "text": "Pinch and hold while tongue works a second place.", "options": ["Pass", "Release early", "Switch places"]},
                {"id": 6, "text": "Spank → ice the sting → warm again with mouth.", "options": ["Pass", "Skip one step", "Change sequence"]},
                {"id": 7, "text": "Water or ice dripping, followed by heavy tongue.", "options": ["Pass", "Lighter tongue", "Stop at dripping"]},
                {"id": 8, "text": "Wax one side, ice the other, tongue decides.", "options": ["Pass", "One temperature only", "Both choose sides"]},
                {"id": 9, "text": "Pinch path + light spank over it + full lick.", "options": ["Pass", "Remove spank", "Remove pinch"]},
                {"id": 10, "text": "Keep ice in place while tongue works elsewhere.", "options": ["Pass", "Move the ice", "Switch focus"]},
                {"id": 11, "text": "Layer in any order you both agree: pinch, wax (safe), ice, tongue.", "options": ["Pass", "Use only two", "Use all four"]},
                {"id": 12, "text": "Spank until warm, then taste the heat slowly.", "options": ["Pass", "Stop at warm", "Add ice first"]},
                {"id": 13, "text": "Ice between lips, pressed and dragged, then pure tongue.", "options": ["Pass", "Keep ice longer", "Immediate tongue"]},
                {"id": 14, "text": "Pinch and lick on two different spots at once.", "options": ["Pass", "One spot only", "Switch who does what"]},
                {"id": 15, "text": "Water droplets + safe wax nearby + tongue closes the gap.", "options": ["Pass", "No wax", "No water"]},
                {"id": 16, "text": "Spank → pause → ice → pause → tongue.", "options": ["Pass", "Remove pauses", "Shorten the chain"]},
                {"id": 17, "text": "Light pinch trail → ice → full mouth.", "options": ["Pass", "Softer", "Skip pinches"]},
                {"id": 18, "text": "Controlled wax, ice soothe, tongue claims.", "options": ["Pass", "Ice + tongue only", "Wax + tongue only"]},
                {"id": 19, "text": "Hold with pinches while tongue finishes the sensation.", "options": ["Pass", "No holding", "Lighter hold"]},
                {"id": 20, "text": "Final open layer: any combination of ice, water, safe wax, pinching, spanking, licking — both players choose what stays and what goes.", "options": ["Pass", "Build together", "End whenever either person wants"]}
            ]
        }
    }
}
