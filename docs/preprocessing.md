# Text Preprocessing Module

## Purpose

The OCR output extracted from screenshots often contains inconsistent formatting, uppercase letters, and unnecessary whitespace.

This module cleans OCR text before it is passed to the semantic search engine.

---

## Operations Performed

### 1. Lowercase Conversion

Input:

PAYING SWETHA MOBILES

Output:

paying swetha mobiles

---

### 2. Whitespace Normalization

Input:

PAYING     SWETHA      MOBILES

Output:

paying swetha mobiles

---

## Example

Raw OCR Output:

PAYING SWETHA MOBILES
9790
ICICI BANK

Processed Output:

paying swetha mobiles 9790 icici bank

---

## Role In SnapMind AI

Screenshot

↓

OCR

↓

Text Preprocessing

↓

Embeddings

↓

Semantic Search

This module improves text consistency and prepares OCR output for AI-powered search.
