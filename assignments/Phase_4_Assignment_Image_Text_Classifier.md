# Phase 4 Assignment: Image or Text Classifier

## Objective
Build a deep learning classifier for either images or text (your choice).

## Option A: Image Classifier
**Dataset**: CIFAR-10, Fashion-MNIST, or your own dataset (200+ images, 3+ classes)

**Requirements**:
1. Build a CNN with at least 3 convolutional layers
2. Apply data augmentation
3. Use transfer learning with a pretrained model (ResNet, EfficientNet, or VGG)
4. Compare scratch CNN vs. transfer learning (accuracy, training time)
5. Visualize: training curves, confusion matrix, 5 misclassified examples

## Option B: Text Classifier
**Dataset**: IMDB, Amazon reviews, Yelp, or your own dataset (1000+ samples, 2+ classes)

**Requirements**:
1. Text preprocessing pipeline (tokenization, cleaning, padding)
2. Train an LSTM or GRU model
3. Fine-tune a HuggingFace transformer model (DistilBERT recommended)
4. Compare LSTM vs. Transformer (F1, training time, model size)
5. Visualize: attention weights, confusion matrix, misclassified examples

## Both Options Must Include
- Clear train/validation/test split
- At least 3 evaluation metrics
- Discussion of overfitting and how you addressed it
- Model saved and loadable for inference

## Deliverables
- Jupyter Notebook
- Saved model file (`model.h5` or `model.pt`)
- GitHub repository
- 1-page PDF summary of results

## Grading
| Criterion | Points |
|-----------|--------|
| Model architecture | 25 |
| Training and evaluation | 25 |
| Comparison analysis | 25 |
| Visualizations | 15 |
| Documentation | 10 |
| **Total** | **100** |
