# 🧠 Transformer from scratch (PyTorch)

## 🎯 Objectif
Coder un **Transformer de zéro en PyTorch**, pour comprendre l'architecture qui est derrière *tous* les modèles IA modernes — pas juste l'utiliser.

## 📚 Ressource principale
- **Umar Jamil — « Coding a Transformer from scratch on PyTorch, with full explanation, training and inference »**
  → https://www.youtube.com/watch?v=ISNdQcPhsts *(17 chapitres, explication complète + entraînement + inférence)*
- Son GitHub (implémentation de référence) → https://github.com/hkproj *(repo `pytorch-transformer`, « Attention is all you need »)*
- Le papier original : *Attention Is All You Need* → https://arxiv.org/abs/1706.03762

## 🧩 Ce que je vais implémenter
- Input embeddings + **positional encoding**
- **Multi-head attention** (le cœur)
- Blocs **encoder** et **decoder**
- Projection layer
- **Boucle d'entraînement** complète (loss, optimizer)
- **Pipeline d'inférence** sur des vraies séquences
- Bonus : **visualisation des attention scores**
- Cas d'usage du cours : traduction (dataset + tokenizer HuggingFace)

## 💼 Pourquoi ce projet (double intérêt)
1. **Exam ML (CS-233)** — ça recoupe directement le cours ; implémenter à la main = la meilleure façon de vraiment comprendre.
2. **GitHub / stages** — mon dossier CV a le point ouvert *« créer mon GitHub et le lier »* pour les candidatures **Google / Meta été 2026**. Un Transformer from scratch bien documenté est exactement le type de repo qui fait recruter.

## 🗺️ Plan (milestones)
- [ ] 1. Setup env (Python, PyTorch, venv) + squelette de repo
- [ ] 2. Embeddings + positional encoding
- [ ] 3. Multi-head attention
- [ ] 4. Encoder / Decoder blocks + projection
- [ ] 5. Boucle d'entraînement (dataset + tokenizer)
- [ ] 6. Inférence + visualisation de l'attention
- [ ] 7. README propre, tests, **push GitHub**

## 💬 Prompt de démarrage (à coller dans le nouveau chat)
> Je veux coder un Transformer from scratch en PyTorch, en suivant le cours d'Umar Jamil (https://www.youtube.com/watch?v=ISNdQcPhsts). Objectif : vraiment comprendre l'architecture (pas juste copier), parce que ça recoupe mon exam de ML à l'EPFL et que je veux en faire un repo GitHub propre pour mes candidatures de stage. Lis le README de ce dossier, puis propose-moi comment on attaque le milestone 1, et guide-moi étape par étape en m'expliquant le *pourquoi* de chaque brique.

---
_Créé le 2026-07-13. Origine : TikTok @volkan.js « 4 Essential AI/ML Projects for CS Majors »._
