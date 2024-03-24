def read_input():
    global W, H, D, M, grid, assigned, C, B, S

    # Données de grille
    W, H = map(int,
               input("Lire la largeur et la hauteur du bureau :>").split())  # Lire la largeur et la hauteur du bureau
    grid = [input("Lire la carte :>") for _ in range(H)]  # Lire la carte
    assigned = [[-1] * W for _ in range(H)]

    # Données des développeurs
    D = int(input("Lire les développeurs :>"))  # Lire les développeurs
    C = [None] * D  # Allocate developer's info
    B = [None] * D
    S = [set() for _ in range(D)]

    # Mapper les compétences à l'identifiant d'entier
    scount = 1  # compteur de compétences
    skill_ids = {}  # compétences en mappage d'entiers

    # Lire le développeur's company, bonus, and skills
    for i in range(D):
        C[i], B[i], Is = input("le développeur's company:>").split()
        B[i] = int(B[i])
        Is = int(Is)
        for _ in range(Is):
            s = input("Lire les compétences :>")
            if s not in skill_ids:  # compétences non cartographiées
                skill_ids[s] = scount  # a attribué un index
                scount += 1
            S[i].add(skill_ids[s])

    # Données des gestionnaires
    M = int(input("Lire les gestionnaires :>"))  # Lire les gestionnaires
    C.extend([None] * M)
    B.extend([None] * M)


print(read_input())