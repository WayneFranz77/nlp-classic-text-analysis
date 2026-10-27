from src.preprocessing import (
    load_text,
    word_sentence_tokenize
)

from src.analysis import (
    pos_tag_text,
    analyze_np_chunks,
    analyze_vp_chunks
)

from src.chunking import (
    create_np_parser,
    create_vp_parser,
    chunk_sentences
)

from src.utils import (
    save_chunk_report,
    save_chunk_csv,
    save_frequency_chart
)


def main():

    # Load text
    text = load_text(
        "data/raw/dorian_gray.txt"
    )

    # Tokenize text
    word_tokenized_text = (
        word_sentence_tokenize(text)
    )

    print(
        f"Tokenized {len(word_tokenized_text)} sentences."
    )

    # POS tagging
    pos_tagged_text = (
        pos_tag_text(word_tokenized_text)
    )

    print(
        f"POS tagged {len(pos_tagged_text)} sentences."
    )

    # Create parsers
    np_parser = create_np_parser()
    vp_parser = create_vp_parser()

    # Chunk text
    np_chunked_text = chunk_sentences(
        pos_tagged_text,
        np_parser
    )

    vp_chunked_text = chunk_sentences(
        pos_tagged_text,
        vp_parser
    )

    # Analyze chunks
    most_common_np_chunks = analyze_np_chunks(
        np_chunked_text
    )

    most_common_vp_chunks = analyze_vp_chunks(
        vp_chunked_text
    )

    # Save report
    save_chunk_report(
        most_common_np_chunks,
        most_common_vp_chunks,
        "outputs/reports/chunk_analysis_report.txt"
    )

    # Save CSV files
    save_chunk_csv(
        most_common_np_chunks,
        "outputs/results/noun_phrase_counts.csv"
    )

    save_chunk_csv(
        most_common_vp_chunks,
        "outputs/results/verb_phrase_counts.csv"
    )

    # Save charts
    save_frequency_chart(
        most_common_np_chunks,
        "Top Noun Phrase Chunks",
        "outputs/figures/noun_phrase_frequency.png"
    )

    save_frequency_chart(
        most_common_vp_chunks,
        "Top Verb Phrase Chunks",
        "outputs/figures/verb_phrase_frequency.png"
    )

    # Display results
    print("\nTop Noun Phrase Chunks:")
    print("-" * 40)

    for chunk, count in most_common_np_chunks[:10]:
        print(
            f"{count:>5} | {chunk}"
        )

    print("\nTop Verb Phrase Chunks:")
    print("-" * 40)

    for chunk, count in most_common_vp_chunks[:10]:
        print(
            f"{count:>5} | {chunk}"
        )

    print("\nResults saved successfully.")

    print(
        "\nReport: outputs/reports/chunk_analysis_report.txt"
    )

    print(
        "CSV: outputs/results/noun_phrase_counts.csv"
    )

    print(
        "CSV: outputs/results/verb_phrase_counts.csv"
    )

    print(
        "Figure: outputs/figures/noun_phrase_frequency.png"
    )

    print(
        "Figure: outputs/figures/verb_phrase_frequency.png"
    )


if __name__ == "__main__":
    main()
