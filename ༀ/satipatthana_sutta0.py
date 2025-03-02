"""
Satipatthana Sutta: The Four Foundations of Mindfulness
A Python interpretation of the Buddha's discourse on mindfulness

This script embodies the four foundations of mindfulness:
1. Contemplation of the body (kayanupassana)
2. Contemplation of feelings (vedananupassana)
3. Contemplation of mind (cittanupassana)
4. Contemplation of mind objects/phenomena (dhammanupassana)

May all beings who read this code cultivate mindfulness and compassion.
"""

import time
from typing import List, Dict, Callable, Optional, Any
import random


class Mindfulness:
    """
    The practice of mindfulness as taught in the Satipatthana Sutta.
    Each method represents an aspect of the four foundations of mindfulness.
    """
    
    def __init__(self, practitioner_name: Optional[str] = None):
        """Initialize mindfulness practice with awareness of the practitioner."""
        self.practitioner = practitioner_name or "mindful being"
        self.present_moment = time.time()
        self.breath_count = 0
        self.state_of_mind = "beginning awareness"
        
        # The hindrances to mindfulness
        self.hindrances = {
            "sensory_desire": 0,
            "aversion": 0,
            "sloth_torpor": 0,
            "restlessness_worry": 0,
            "doubt": 0
        }
        
        print(f"Mindfulness practice begun. Welcome, {self.practitioner}.")
        print("Remember: Be present, be aware, be compassionate.")
    
    def mindfulness_of_breathing(self, breaths: int = 10) -> None:
        """
        Mindfulness of breathing (anapanasati) - a fundamental practice
        where attention is placed on the sensation of breath.
        """
        print("\n=== Mindfulness of Breathing ===")
        print("Settling into awareness of the breath...")
        
        for i in range(breaths):
            self.breath_count += 1
            self.present_moment = time.time()
            
            # Simulating inhalation and exhalation
            print(f"Breath {i+1}: Breathing in... I know I am breathing in.")
            time.sleep(0.5)  # Symbolic pause for mindful awareness
            print(f"Breath {i+1}: Breathing out... I know I am breathing out.")
            time.sleep(0.5)  # Symbolic pause for mindful awareness
            
            # Every third breath, introduce a mindfulness contemplation
            if (i + 1) % 3 == 0:
                contemplation = random.choice([
                    "Aware of my whole body, I breathe in... Aware of my whole body, I breathe out.",
                    "Calming my bodily formation, I breathe in... Calming my bodily formation, I breathe out.",
                    "Experiencing joy, I breathe in... Experiencing joy, I breathe out.",
                    "Experiencing happiness, I breathe in... Experiencing happiness, I breathe out.",
                    "Aware of impermanence, I breathe in... Aware of impermanence, I breathe out."
                ])
                print(contemplation)
        
        print(f"Completed {breaths} mindful breaths.")
        print("Notice how the mind and body feel now compared to before.")
    
    def body_contemplation(self) -> None:
        """
        First Foundation: Contemplation of the Body (Kayanupassana)
        Awareness of the body's positions, movements, and composition.
        """
        print("\n=== Contemplation of the Body ===")
        
        # Four Postures
        postures = ["sitting", "standing", "walking", "lying down"]
        current_posture = random.choice(postures)
        print(f"Awareness of posture: I am {current_posture}.")
        print("Whatever posture this body is in, I observe it with clear comprehension.")
        
        # Body Parts Reflection
        body_parts = [
            "head hair", "body hair", "nails", "teeth", "skin",
            "flesh", "sinews", "bones", "bone marrow", "kidneys",
            "heart", "liver", "diaphragm", "spleen", "lungs",
            "intestines", "mesentery", "stomach", "feces", "bile",
            "phlegm", "pus", "blood", "sweat", "fat",
            "tears", "grease", "saliva", "mucus", "fluid", "urine"
        ]
        
        print("Reflecting on the body's composition:")
        print("This body contains various elements and is not self.")
        for i, part in enumerate(random.sample(body_parts, 5)):
            print(f"{i+1}. {part}")
        
        # Elements Contemplation
        elements = ["earth (solidity)", "water (fluidity)", "fire (temperature)", "air (movement)"]
        print("\nContemplating the four elements within this body:")
        for element in elements:
            print(f"- The {element} element is present in this body.")
        
        print("\nThrough this contemplation, I see the body as it truly is:")
        print("Impermanent, subject to change, not-self.")
    
    def feelings_contemplation(self) -> Dict[str, int]:
        """
        Second Foundation: Contemplation of Feelings (Vedananupassana)
        Awareness of pleasant, unpleasant, and neutral feelings.
        """
        print("\n=== Contemplation of Feelings ===")
        
        # Generate random feeling states for demonstration
        feeling_types = {
            "pleasant": random.randint(1, 10),
            "unpleasant": random.randint(1, 10),
            "neutral": random.randint(1, 10)
        }
        
        dominant_feeling = max(feeling_types, key=feeling_types.get)
        
        print(f"At this moment, I observe that these feelings are present:")
        for feeling, intensity in feeling_types.items():
            print(f"- {feeling.capitalize()} feelings: {'●' * intensity}")
        
        print(f"\nThe dominant feeling tone is: {dominant_feeling}")
        print("I observe these feelings with mindfulness:")
        print("- They arise due to conditions")
        print("- They are impermanent")
        print("- They are not 'me' or 'mine'")
        print("- They change and transform")
        
        return feeling_types
    
    def mind_contemplation(self) -> None:
        """
        Third Foundation: Contemplation of Mind (Cittanupassana)
        Awareness of the state of mind and mental qualities.
        """
        print("\n=== Contemplation of Mind ===")
        
        # Possible mind states from the sutta
        mind_states = [
            ("with desire", "without desire"),
            ("with aversion", "without aversion"),
            ("with delusion", "without delusion"),
            ("contracted", "expanded"),
            ("exalted", "unexalted"),
            ("surpassable", "unsurpassable"),
            ("concentrated", "unconcentrated"),
            ("liberated", "unliberated")
        ]
        
        print("Observing the current state of mind:")
        current_states = []
        
        for state_pair in mind_states:
            # Randomly choose one state from each pair for demonstration
            selected = random.choice(state_pair)
            current_states.append(selected)
            
        # Display three random states for simplicity
        sample_states = random.sample(current_states, 3)
        for state in sample_states:
            print(f"- Mind is {state}")
        
        print("\nI observe that these mind states are:")
        print("- Constantly changing")
        print("- Arising and passing away due to conditions")
        print("- Not a fixed self or identity")
        
        # Update the state of mind
        self.state_of_mind = random.choice([
            "clear and aware", "momentarily concentrated", 
            "open and receptive", "calm and collected"
        ])
        print(f"\nThrough this contemplation, the mind becomes: {self.state_of_mind}")
    
    def dharma_contemplation(self) -> None:
        """
        Fourth Foundation: Contemplation of Mind Objects/Phenomena (Dhammanupassana)
        Awareness of various categories of experience as taught in the Buddha's teachings.
        """
        print("\n=== Contemplation of Mind Objects (Dhamma) ===")
        
        # Choose one aspect of dhamma contemplation to focus on
        contemplations = [
            self._contemplate_hindrances,
            self._contemplate_aggregates,
            self._contemplate_sense_bases,
            self._contemplate_bojjhangas,
            self._contemplate_four_noble_truths
        ]
        
        chosen_contemplation = random.choice(contemplations)
        chosen_contemplation()
    
    def _contemplate_hindrances(self) -> None:
        """Contemplation of the Five Hindrances."""
        print("Contemplating the Five Hindrances:")
        
        # Randomly set hindrance levels for demonstration
        for hindrance in self.hindrances:
            self.hindrances[hindrance] = random.randint(0, 10)
        
        for hindrance, level in self.hindrances.items():
            hindrance_name = hindrance.replace("_", " ").title()
            presence = "present" if level > 3 else "not strongly present"
            print(f"- {hindrance_name}: {presence} (level: {level}/10)")
            
            if level > 3:
                print(f"  I recognize how {hindrance_name.lower()} arises and how it can be abandoned.")
        
        print("\nKnowing these hindrances as they are leads to freedom from them.")
    
    def _contemplate_aggregates(self) -> None:
        """Contemplation of the Five Aggregates of Clinging."""
        print("Contemplating the Five Aggregates:")
        
        aggregates = {
            "form": "The physical body and material phenomena",
            "feeling": "Pleasant, unpleasant, and neutral sensations",
            "perception": "Recognition and interpretation of sense objects",
            "mental formations": "Volition, attention, and other mental factors",
            "consciousness": "Awareness through the six sense doors"
        }
        
        for aggregate, description in aggregates.items():
            print(f"- {aggregate.title()}: {description}")
            print(f"  I observe: this is not mine, this is not me, this is not myself.")
        
        print("\nSeeing the aggregates as impermanent, subject to suffering, and not-self.")
    
    def _contemplate_sense_bases(self) -> None:
        """Contemplation of the Six Internal and External Sense Bases."""
        print("Contemplating the Six Sense Bases:")
        
        sense_bases = [
            ("eye", "visible forms"),
            ("ear", "sounds"),
            ("nose", "odors"),
            ("tongue", "flavors"),
            ("body", "tangible objects"),
            ("mind", "mental objects")
        ]
        
        # Choose random sense bases to contemplate
        chosen_bases = random.sample(sense_bases, 3)
        
        for internal, external in chosen_bases:
            print(f"- {internal.title()} and {external}:")
            print(f"  I understand how these interact to produce contact and feeling.")
            print(f"  I observe how attachments can arise dependent on these, and how they can be released.")
        
        print("\nUnderstanding sense bases leads to freedom from bondage to sensory experience.")
    
    def _contemplate_bojjhangas(self) -> None:
        """Contemplation of the Seven Factors of Enlightenment."""
        print("Contemplating the Seven Factors of Enlightenment (Bojjhangas):")
        
        bojjhangas = [
            "mindfulness",
            "investigation of phenomena",
            "energy",
            "joy",
            "tranquility",
            "concentration",
            "equanimity"
        ]
        
        # Assign random levels to each factor
        bojjhanga_levels = {factor: random.randint(1, 10) for factor in bojjhangas}
        
        for factor, level in bojjhanga_levels.items():
            status = "present and developed" if level > 5 else "present but undeveloped"
            print(f"- {factor.title()}: {status} (level: {level}/10)")
            
            if level <= 5:
                print(f"  I understand how the factor of {factor} can be further developed.")
        
        print("\nCultivating these factors leads to wisdom and liberation.")
    
    def _contemplate_four_noble_truths(self) -> None:
        """Contemplation of the Four Noble Truths."""
        print("Contemplating the Four Noble Truths:")
        
        noble_truths = [
            "The truth of suffering (dukkha): Life contains unsatisfactoriness, stress, and suffering.",
            "The truth of the origin of suffering (samudaya): Craving and ignorance lead to suffering.",
            "The truth of the cessation of suffering (nirodha): There is an end to suffering.",
            "The truth of the path leading to cessation (magga): The Eightfold Path leads to the end of suffering."
        ]
        
        for truth in noble_truths:
            print(f"- {truth}")
            
        print("\nUnderstanding these truths directly leads to liberation.")
    
    def establish_mindfulness(self, duration_minutes: int = 10) -> None:
        """
        Practice the full Satipatthana meditation for the specified duration.
        This is the main method that integrates all four foundations.
        """
        print(f"\n==== Beginning Satipatthana Practice ({duration_minutes} minutes) ====")
        print("Establishing mindfulness before me...")
        print("I dwell ardent, clearly comprehending, and mindful, free from desires and discontent.")
        
        # Symbolic time passing (in reality, this would be spent in actual meditation)
        start_time = time.time()
        elapsed_minutes = 0
        
        # Divide the practice time among the foundations
        foundation_time = duration_minutes / 4
        
        # Practice each foundation
        self.mindfulness_of_breathing(breaths=5)
        print(f"\n{elapsed_minutes + foundation_time} minutes elapsed...")
        elapsed_minutes += foundation_time
        
        self.body_contemplation()
        print(f"\n{elapsed_minutes + foundation_time} minutes elapsed...")
        elapsed_minutes += foundation_time
        
        self.feelings_contemplation()
        print(f"\n{elapsed_minutes + foundation_time} minutes elapsed...")
        elapsed_minutes += foundation_time
        
        self.mind_contemplation()
        self.dharma_contemplation()
        
        # Conclude the practice
        end_time = time.time()
        actual_time = (end_time - start_time) / 60  # Convert to minutes
        
        print("\n==== Concluding Satipatthana Practice ====")
        print(f"Practice completed (symbolic {duration_minutes} minutes, actual {actual_time:.2f} minutes).")
        print("\nMay this practice benefit all beings.")
        print("May all beings be free from suffering.")
        print("May all beings be peaceful.")
        print("May all beings be liberated.")
    
    def cultivate_insight(self) -> List[str]:
        """
        Develop insights through sustained mindfulness practice.
        Returns a list of insights that might arise through practice.
        """
        insights = [
            "All conditioned things are impermanent (anicca).",
            "Where there is attachment, there is suffering (dukkha).",
            "All phenomena are without an inherent self (anatta).",
            "With mindfulness, we see things as they really are.",
            "Peace comes from accepting the present moment fully.",
            "Compassion arises naturally with clear seeing.",
            "The mind and body are interdependent processes, not separate entities.",
            "Freedom is found in non-clinging to experience."
        ]
        
        print("\n=== Insights from Mindfulness Practice ===")
        chosen_insights = random.sample(insights, 3)
        
        for i, insight in enumerate(chosen_insights, 1):
            print(f"{i}. {insight}")
        
        print("\nThese insights arise not from thinking, but from direct experience.")
        print("They are to be realized, not merely understood intellectually.")
        
        return chosen_insights
    
    def apply_to_daily_life(self) -> None:
        """
        Practical applications of mindfulness in daily activities.
        As emphasized in the Satipatthana Sutta, mindfulness should extend beyond formal practice.
        """
        print("\n=== Applying Mindfulness in Daily Life ===")
        
        daily_activities = [
            "eating mindfully, aware of each bite and taste",
            "walking with awareness of each step and the body's movement",
            "speaking with conscious awareness of words and their impact",
            "listening deeply to others without planning what to say next",
            "working with full attention to the task at hand",
            "being aware of thoughts and emotions as they arise during the day",
            "noting transitions between activities with mindful awareness",
            "observing reactions to pleasant and unpleasant experiences"
        ]
        
        print("The Buddha taught mindfulness to be practiced at all times, in all activities.")
        print("Here are ways to bring mindfulness into daily life:")
        
        for i, activity in enumerate(random.sample(daily_activities, 4), 1):
            print(f"{i}. {activity.capitalize()}")
        
        print("\nMindfulness is not limited to formal meditation.")
        print("Every moment is an opportunity for mindfulness and compassion.")


def main():
    """
    Main function to demonstrate the teachings of the Satipatthana Sutta.
    """
    print("=" * 80)
    print("THE FOUR FOUNDATIONS OF MINDFULNESS (SATIPATTHANA SUTTA)")
    print("A contemplative journey through the Buddha's teachings on mindfulness")
    print("=" * 80)
    print("\nThis program embodies the essence of the Buddha's discourse on mindfulness.")
    print("As you read and engage with this code, may you cultivate awareness and compassion.")
    print("\n'Here, monks, a practitioner dwells contemplating the body as body, feelings as")
    print("feelings, mind as mind, and mind-objects as mind-objects, ardent, clearly")
    print("comprehending, and mindful, having put away covetousness and grief for the world.'")
    print("\nMay all beings benefit from this contemplation.\n")
    
    # Optional: Ask for practitioner's name
    try:
        name = input("If you wish, enter your name (or press Enter to continue): ").strip()
    except:
        name = None  # Handle case where input isn't available
    
    # Create mindfulness object and begin practice
    practice = Mindfulness(name if name else None)
    
    try:
        # Brief demonstration of the practice
        practice.establish_mindfulness(duration_minutes=5)
        practice.cultivate_insight()
        practice.apply_to_daily_life()
        
        print("\n" + "=" * 80)
        print("CONCLUSION")
        print("=" * 80)
        print("\nThe Buddha concluded the Satipatthana Sutta with this promise:")
        print("\n'If anyone should develop these four foundations of mindfulness in such a way")
        print("for seven years, one of two fruits could be expected: either final knowledge")
        print("in this very life or, if there is a trace of clinging left, non-return.'")
        print("\nThank you for engaging with this teaching. May your mindfulness practice flourish.")
        print("May all beings be happy, peaceful, and liberated.")
        
    except KeyboardInterrupt:
        print("\n\nPractice paused. Remember that mindfulness continues beyond formal practice.")
        print("May you be well, peaceful, and free from suffering.")


if __name__ == "__main__":
    main()
