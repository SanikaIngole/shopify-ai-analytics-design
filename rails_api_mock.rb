class QuestionsController < ApplicationController
  def create
    render json: {
      answer: "Reorder 70 units based on last 30 days sales",
      confidence: "medium"
    }
  end
end
