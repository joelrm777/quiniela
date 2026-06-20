import sys
import os

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

from scoring import calculate_points

def test_case(home_pred, away_pred, home_real, away_real, expected_total, description):
    res = calculate_points(home_pred, away_pred, home_real, away_real)
    assert res["total_points"] == expected_total, (
        f"FAILED: {description}. Predicted: {home_pred}-{away_pred}, Real: {home_real}-{away_real}. "
        f"Expected {expected_total} points, got {res['total_points']} ({res})"
    )
    print(f"PASSED: {description:45s} | Pred: {home_pred}-{away_pred} | Real: {home_real}-{away_real} | Pts: {res['total_points']}")

if __name__ == "__main__":
    print("Iniciando pruebas unitarias de la logica de puntuacion...")
    print("-" * 80)
    
    try:
        # Case 1: Exact score match (winner local)
        # Outcome correct (3) + Exact match (2) + Home goals (1) + Away goals (1) = 7
        test_case(2, 1, 2, 1, 7, "Marcador exacto con victoria local")
        
        # Case 2: Exact score match (draw)
        # Outcome correct (3) + Exact match (2) + Home goals (1) + Away goals (1) = 7
        test_case(1, 1, 1, 1, 7, "Marcador exacto con empate")

        # Case 3: Guesses local winner, guesses local goals, wrong away goals
        # Outcome correct (3) + Exact (0) + Home goals (1) + Away goals (0) = 4
        test_case(2, 1, 2, 0, 4, "Acierto resultado y goles de local")

        # Case 4: Guesses draw outcome, incorrect goals
        # Outcome correct (3) + Exact (0) + Home goals (0) + Away goals (0) = 3
        test_case(1, 1, 2, 2, 3, "Acierto resultado de empate con goles errados")

        # Case 5: Guesses wrong outcome, guesses away goals correctly (predicted visitor wins 1-2, real local wins 3-2)
        # Outcome (0) + Exact (0) + Home goals (0) + Away goals (1) = 1
        test_case(1, 2, 3, 2, 1, "Acierto solo de goles visitante (outcome incorrecto)")

        # Case 6: Completely wrong
        # Outcome (0) + Exact (0) + Home goals (0) + Away goals (0) = 0
        test_case(0, 0, 2, 1, 0, "Ningun acierto")
        
        # Case 7: Wrong outcome, wrong exact, but guesses local goals correctly
        # Outcome (0) + Exact (0) + Home goals (1) + Away goals (0) = 1
        test_case(1, 1, 1, 0, 1, "Acierto solo de goles local (empate pred vs local real)")

        print("-" * 80)
        print("TODAS LAS PRUEBAS DE PUNTUACION SE COMPLETARON CON EXITO!")
    except AssertionError as e:
        print(e)
        sys.exit(1)
