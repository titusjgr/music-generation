from fastai.text import AWD_LSTM, TextLMDataBunch, language_model_learner, load_data
import os


def main():

    text_dir = './midi_text'

    if 'data_lm_export.pkl' in os.listdir(text_dir):
        data_lm = load_data(text_dir, 'data_lm_export.pkl')
    else:
        data_lm = TextLMDataBunch.from_folder(text_dir)
        data_lm.save('data_lm_export.pkl')

    learner = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.5)

    learner.unfreeze()
    learner.fit_one_cycle(200, 1e-2)

    learner.save_encoder('AWD_LSTM')


if __name__ == '__main__':
    main()
